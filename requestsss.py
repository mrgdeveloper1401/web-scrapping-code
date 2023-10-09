import requests


# url = 'https://daneshkar.net/'


# responce = requests.get(url)
# responce = requests.put(url)
# print(responce)
# print(responce.reason)

# print(dir(responce))
# print(responce.json)
# print(responce.url)
# print(responce.status_code)
# print(responce.request)
# print(dir(responce.request))
# print(responce.request.headers)
# print(dir(responce))
# print(responce.reason)
# print(responce.text)

# with open('text.txt', 'w') as file:
#     file.write(responce.text)

url = 'https://sess.shirazu.ac.ir/Sess/13624131273'

responce = requests.post(url, auth=('s9974261', 'zxcvbnm.236'))
# print(responce.headers['Set-Cookie'])
# print(responce.cookies)
print(responce.status_code)