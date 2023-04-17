import requests
data = {
	"height": 172,
	"weight": 74
}

resp = requests.post('http://localhost:8000/size', json=data)
print(resp.json())