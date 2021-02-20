import json, requests
import re
import geoip2.database
from flask import url_for
import os

def getIPAddress():
  ip = requests.get('https://checkip.amazonaws.com').text.strip()
  print(ip)
  return ip

def getCityName(ip:str):
  curr_path = os.path.split(os.path.realpath(__file__))[0]
  reader = geoip2.database.Reader(curr_path + "/../static/GeoLite2-City.mmdb")
  response = reader.city(ip)
  return response.city.names["zh-CN"][:-1]

def getLocalCityName():
  return getCityName(getIPAddress())

def getWeather(city_name:str):
  '''
  get weather of a specify city 
    Args:
      city_name: city name
  '''
  api_url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city_name
  response = requests.get(api_url)
  response.raise_for_status()
  weather_data = json.loads(response.text)
  w = weather_data["data"]

  res = []
  for i in range(len(w['forecast'])):
    curr_weather_data = {}
    # curr_date = re.findall(r"\d+\.?\d*",w['forecast'][i]['date'])[0]
    curr_weather_data["date"] = w['forecast'][i]['date']

    curr_high_temp = re.findall(r"\d+\.?\d*",w['forecast'][i]['high'])[0]
    curr_weather_data["high_temp"] = curr_high_temp

    curr_low_tmp= re.findall(r"\d+\.?\d*",w['forecast'][i]['low'])[0]
    curr_weather_data["low_temp"] = curr_low_tmp

    curr_weather_data["type"] = w['forecast'][i]['type']
    
    # print("日期：" + dates[i])
    # print("\t温度：最低" + low_temps[i] + '~最高' + high_temps[i] + '')
    # print("\t天气：" + weathers[i])
    # print("")
    res.append(curr_weather_data)
  return res

if __name__ == "__main__":
  print(getLocalCityName())