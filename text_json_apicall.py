import json
import requests


parsed_data = {}

with open('jsonapi.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    key, value = line.strip().split('=')
    parsed_data[key] = value




#data to json format
json_data = json.dumps(parsed_data)



#json - api call

url = 'https://reqres.in/api/users'

headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json_data)



if response.status_code == 201:
    print('Data sent successfully')
else:
    print('Failed to send data. Status code:', response.status_code)
