import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
second_response = response
three_response = response
four_response = response






#for response in first_response:
#    print(second_response.url)

print(first_response.url)
print(second_response.url)
print(three_response.url)
print(four_response.url)
