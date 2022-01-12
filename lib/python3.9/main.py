import requests
import json
# from datetime import datetime as dt


# print(dt.now().today())


WEATHER_KEY="my_weather_key"
WEATHER_URL="opendata.cwb.gov.tw/api"
#
response=requests.get(f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={WEATHER_KEY}&format=JSON")
print(response)
datas = response.json()
#
# print(datas)
#
county = input("請輸入想查詢的縣市：")
#
# # print(datas['records']['location'][0])
#
column=['天氣狀況','最低溫','最高溫','舒適度','降雨機率']
order=[0,2,4,3,1]

if "台" in county:
    county = county.replace('台',"臺")
for data in datas['records']['location']:
    if county in data['locationName']:
        print(data['locationName'])
        for i in range(len(order)):
            print(column[i], end=':')
            print(data['weatherElement'][order[i]]['time'][0]['parameter']['parameterName'])
        break
else:
    print("請確認縣市名稱是否輸入正確")
    if datas['records']['location']['locationName']=="桃園市":
        print(data)
    if county in datas['records']['location']['locationName']:
        print(datas['records']['location']['weatherElement'])




