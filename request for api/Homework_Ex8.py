import json
import requests

request_body = {"token": "QN1ojNzoTNxAyMx0iMx0SMyAjM"}

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=request_body)

string_as_json_format = '{"status":"Job is ready"}'

obj = json.loads(string_as_json_format)

key = "status"

if key in obj:
    print(obj[key])
else:
    print(f"Не правильный {key}")