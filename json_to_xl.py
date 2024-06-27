import json
import pandas as pd
import requests

def from_api_to_excel(urlapi,genexcelfile):
    try:
        response=requests.get(urlapi)

        json_data=response.json()

        if 'data' in json_data:
            results=json_data['data']

            df=pd.DataFrame(results)
            df.to_excel(genexcelfile, index=False , sheet_name='data_for_api_practice')
            print(f"Data successfully written to {genexcelfile}")

        else:
             print("No data to write or 'results' key not found in JSON data.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == '__main__':
    url = 'https://reqres.in/api/users'
    excelfile = 'datafromapi.xlsx'

    from_api_to_excel(url,excelfile)