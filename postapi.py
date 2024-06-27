import requests

new_data = {
    "name": "megala",
    "job": "associate"
}
url = "https://reqres.in/api/users"

response = requests.post(url, json=new_data)
response_json = response.json()
print(response_json)
print(response)
print(response.status_code)