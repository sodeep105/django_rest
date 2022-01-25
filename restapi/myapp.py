import json
import requests

URL = "http://127.0.0.1:8000/student/create"

data = {
    'name': 'Sameen',
    'roll': 123,
    'city': ''
}


json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)

data = r.json()
print(data)
