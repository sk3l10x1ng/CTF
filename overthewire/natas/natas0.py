import requests as r
import re


def auth(username,password,URL):

	with r.session() as s:
		response = s.get(URL, auth =(username,password))
		content =response.text
		print(re.findall("<!--The password for natas1 is (.*) -->", content)[0])

def main():
	username = password = 'natas0'
	URL = f"http://{username}.natas.labs.overthewire.org/"
	results = auth(username,password,URL)
	
main()

