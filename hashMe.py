import requests
import hashlib
import getpass

loginURL = 'https://ringzer0ctf.com/login'
url = 'https://ringzer0team.com/challenges/13'
session = requests.session()

username=input("Enter username:")
password=getpass.getpass("Enter Password:")

loginData = dict(username=username,password=password)
post = session.post(loginURL,data=loginData)
req = session.get(url)
s = req.text.find('----- BEGIN MESSAGE -----<br />') + 35
e = req.text.find('----- END MESSAGE -----',s) - 10
if(e==-11):
    print("Invalid login")
    exit()

data = req.text[s:e]
hData = hashlib.sha512(data.encode('utf-8')).hexdigest()

responseURL = 'https://ringzer0ctf.com/challenges/13/' + str(hData)
res = session.post(responseURL)
s = res.text.find('FLAG-') 
e = res.text.find('</div>',s)
flag = res.text[s:e]
print(flag)
