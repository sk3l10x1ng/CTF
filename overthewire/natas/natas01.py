import requests as r
import re



def auth(username ,password, URL) :
	with r.session() as s :
		resp = s.get(URL, auth=(username,password))
		content = resp.text
		print(re.findall("<!--The password for natas2 is (.*) -->", content)[0])

def main():
	username = 'natas1'
	password = '' # natas1 password obtained from natas0
	URL = f"http://{username}.natas.labs.overthewire.org"
	results = auth(username, password, URL)

main()