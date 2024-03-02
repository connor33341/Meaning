import uuid
import time
import threading
import os
from reason import BabelReason
BABELURL = "https://babelia.libraryofbabel.info/babelia.cgi"
FORCEJOIN = False

class BabelScanner:
    def __init__(self,Number,Threads):
        print(f"[INFO]: Initalizing Babel from {Number}")
        self.Number = Number
        self.Threads = Threads
        self.Delay = 0
        self.ThreadPool = []
    
    def ThreadSetup(self):
        TargetNumber = self.Number + self.Threads
        for i in range(self.Number,TargetNumber):
            print(f"[INFO]: Begining {i}")
            Thread = threading.Thread(target=self.BabelThread,args=[i])
            Thread.start()
        while self.ThreadPool != []:
            i = -1
            for Thread in self.ThreadPool:
                i = i + 1
                if Thread.is_alive():
                    pass
                else:
                    self.ThreadPool[i] = None
            i = -1
            CacheThreadPool = []
            for Object in self.ThreadPool:
                i = i + 1
                if self.ThreadPool[i] == None:
                    pass
                else:
                    CacheThreadPool[len(CacheThreadPool)+1] = Object
            self.ThreadPool = CacheThreadPool
        if self.ThreadPool == []:
            if FORCEJOIN:
                for Thread in threading.enumerate():
                    Thread.join()
            print("[INFO]: Threading cluster ended")
        else:
            raise RuntimeError("[ERROR]: Program relies on the assumption that while self.ThreadPool != [] is ended from the statement being false")

    def BabelThread(self,Number):
        try:
            time.sleep(float(self.Delay))
            ID = uuid.uuid4()
            Dir = f"cache/{ID}/"
            os.makedirs(Dir,exist_ok=False)
            with open(f"{Dir}{Number}.jpg","a") as File:
                File.close()
            BabelReasonClass = BabelReason(Number,BABELURL,ID,Dir)
            BabelReasonClass.GetImage()
        except Exception as Error:
            print(f"[ERROR]: {Error}")

if __name__ == "__main__":
    print("[INFO]: Running")
    with open("start.babelindex","r") as BabelIndex:
        BabelNumber = int(str(BabelIndex.readlines()[0]))
        BabelIndex.close()
    BabelClass = BabelScanner(BabelNumber,25)
    BabelClass.ThreadSetup()