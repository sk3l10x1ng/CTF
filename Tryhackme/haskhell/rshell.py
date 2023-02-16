import requests as r

URL = "http://10.10.10.10:5001/submit"


with open("re.hs","rb") as f:
    try:
        test = r.post(URL,files ={"file":f})
    except r.exceptions.ConnectionError:
        print("Upload completed successfully!")
