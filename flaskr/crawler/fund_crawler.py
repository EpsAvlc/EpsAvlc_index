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

def get_fund_dict():
    web_data = requests.get(fund_site, headers=headers).json()

    fund_list = []

    for item in web_data['data']['items']:
        eva_type = {0:'低估', 1:'适中', 2:'高估', 99:''}
        fund_dict={}
        fund_dict["name"] = item['name']
        fund_dict["pb"] = item['pb']
        fund_dict["pe"] = item['pe']
        fund_dict["roe"] = item['roe']
        fund_dict["eva_type_int"] = eva_type[item["eva_type_int"]]

        fund_list.append(fund_dict)
    return fund_list

def get_specify_fund():
    pass

if __name__ == "__main__":
    pass