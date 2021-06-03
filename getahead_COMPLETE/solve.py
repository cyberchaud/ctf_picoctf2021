import requests
url = 'http://mercury.picoctf.net:34561/index.php'

h = requests.head(url)

#print(h.headers)
print(h.headers.get('flag'))
