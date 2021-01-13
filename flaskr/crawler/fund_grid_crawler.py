import requests
import json

fund_site = 'https://danjuanapp.com/funding/'

headers = {
'Host': 'danjuanapp.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': 'device_id=web_H1esWhJ4Pv; timestamp=1607994009428; acw_tc=2760825916079939915064914efc6128f2c2148c8c4b4b297075e2f078f1fe; channel=1300100141;xq_a_token=dbc50277e5835994661055037927c29431a81695',
'Upgrade-Insecure-Requests': 1,
'Cache-Control': 'max-age=0',
}

def get_fund_net_worth(fund_index):
    web_data = requests.get("https://danjuanapp.com/djapi/fund/" + fund_index, headers=headers).json()
    print(web_data.content)
    return 0

if __name__ == "__main__":
    net_worth = get_fund_net_worth("002708")