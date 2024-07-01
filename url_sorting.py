import requests
import pandas as pd

url = "https://reqres.in/api/users/"
users_data = []

for i in range(1, 11):
    url = url + str(i)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('data', {})
        if data:
            users_data.append(data)

df = pd.DataFrame(users_data)
df_sorted = df.sort_values(by='first_name')

excel_file = "sorted_data.xlsx"
df_sorted.to_excel(excel_file, index=False, engine='openpyxl')

print(f"Data has been successfully written to {excel_file}")