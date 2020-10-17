import requests
import json

fund_site = 'https://danjuanapp.com/djapi/index_eva/dj'

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.5',
'Connection':'keep-alive',
'Host':'danjuanapp.com',
'Upgrade-Insecure-Requests':1,
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}

web_data = requests.get(fund_site, headers=headers).json()
print(web_data)

print("hello")