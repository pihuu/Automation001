# post request
import json, requests, jsonpath

url = 'https://reqres.in/api/users'
json_input = {
    "name": "pikachu",
    "job": "teacher"
}

response = requests.post(url, json_input)
print(response)
print(response.text)
print(response.content)
assert response.status_code == 201
json_output = json.loads(response.text)

print(json_output['job'])
print(json_output['name'])
