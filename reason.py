import requests
class BabelReason:
    def __init__(self,Number,URL,UUID,Dir):
        self.Number = Number
        self.Url = URL
        self.Id = UUID
        self.Dir = Dir
        print(f"[INFO]: Babel Reason INIT {self.Number}")
    
    def GetImage(self):
        Payload = {
            "location": str(self.Number)
        }
        Request = requests.post(self.Url,data=Payload)
        if Request.status_code == 200:
            with open(f"{self.Dir}{self.Number}.jpg","wb") as Image:
                Image.write(str(Request.text).encode(encoding="utf-8"))
                Image.close()
        else:
            print(f"[ERROR]: Request failed {Request.status_code}")