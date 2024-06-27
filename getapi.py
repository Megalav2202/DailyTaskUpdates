import requests
url = 'https://reqres.in/api/users'
response=requests.get(url)
print(response.status_code)
data=response.json()
print(data)
print(response)
