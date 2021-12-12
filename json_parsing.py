import json

string_as_json_format = '{"answ": "Hello, User"}'
obj = json.loads(string_as_json_format)
print(obj['answer2'])

# key = "answer"
#
# if key in obj:
#     print(obj[key])
# else:
#     print(f"Ключа {key} в JSON нет")
