import requests


user = 'admin'
pwd = 'pwd'

payload = {'login': user, 'mdp': pwd}
r = requests.post("http://192.168.99.100:8080", data=payload)


print(r.content)
