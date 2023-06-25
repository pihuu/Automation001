import requests, json

#API URL
url = "https://regres.in/api/users/2"

#Send Get Request
response = requests.get(url)

#Display Response Content
# print(response.content) #body of the response
# print()
print(response.headers) #the header of the body

#validate status code
print(response.status_code)
assert response.status_code == 200
