# level 8 -> level 9

import requests as r 
import re
import base64 as b64

def auth(username, password, URL):

    encoded_secret = '3d3d516343746d4d6d6c315669563362'

    # decode the string from Hex
    decode_hex = bytes.fromhex(encoded_secret).decode('utf-8')

    # reverse a string 
    rev_string = decode_hex[::-1]

    # Decode base64 string
    base64_decode = b64.b64decode(rev_string).decode('utf-8')
    print(f'The decoded the secrect is : {base64_decode}')


    # POST body parameters
    payload = {
        'secret':base64_decode,
        'submit':'Submit+Query'
    }

    with r.session() as s:
        submit_secret = s.post(URL,auth=(username, password),data=payload)
        content =submit_secret.text
        print(re.findall('natas9 is (.*)',content)[0])



def main():
    username = 'natas8'
    password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'
    URL = f"http://{username}.natas.labs.overthewire.org/"
    results = auth(username,password,URL)

main()