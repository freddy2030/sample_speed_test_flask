import requests
 
url = 'http://127.0.0.1:8088/upload/'
files = {'file': open('upload/10M.txt', 'rb')}           
  
response = requests.post(url, files=files)
# response = requests.get(url)
# json = response.json()
print(response.text)


