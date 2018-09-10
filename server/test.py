import requests

data = {"username":"dsad",
		"password":"dsads"}


res = requests.post("http://localhost:8080/api/login",data=data)
print(res.text)
