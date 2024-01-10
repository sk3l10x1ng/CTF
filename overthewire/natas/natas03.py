#pass G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q


import requests as r 

def auth(username, password, URL):

     with r.session() as s:
        response = s.get(URL, auth =(username,password))
        content =response.text
        print(content)


def main():
    username = 'natas3'
    password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'
    URL = f"http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt"
    results = auth(username,password,URL)

main()