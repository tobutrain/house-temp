# -*- coding: utf-8 -*-
import json
import time
import requests
from datetime import datetime

url_1='http://ambidata.io/api/v2/channels/45860/data?&readKey=9a5d4da14c1c1748&n=1'
url_2='http://ambidata.io/api/v2/channels/45861/data?&readKey=bf91b4b4953bb597&n=1'
url_3='http://ambidata.io/api/v2/channels/45862/data?&readKey=3931de126d84d265&n=1'
url_4='http://ambidata.io/api/v2/channels/45863/data?&readKey=7928fdfe2bc2a3cf&n=1'
url_5='http://ambidata.io/api/v2/channels/45864/data?&readKey=fb85ec6edc5e82d6&n=1'
url_6='http://ambidata.io/api/v2/channels/45865/data?&readKey=b91097b4ee8f7320&n=1'
url_7='http://ambidata.io/api/v2/channels/45866/data?&readKey=8e40f5bc024aedd9&n=1'
url_8='http://ambidata.io/api/v2/channels/45867/data?&readKey=269393e563d71a55&n=1'

def get_retry(url, retry_times, errs):
    for t in range(retry_times + 1):
        r = requests.get(url)
        if t < retry_times:
            if r.status_code in errs:
                time.sleep(2)
                continue
        return r

while True:
    arr_1=json.loads(get_retry(url_1,5,[500, 502, 503]).text)[0]
    arr_2=json.loads(get_retry(url_2,5,[500, 502, 503]).text)[0]
    arr_3=json.loads(get_retry(url_3,5,[500, 502, 503]).text)[0]
    arr_4=json.loads(get_retry(url_4,5,[500, 502, 503]).text)[0]
    arr_5=json.loads(get_retry(url_5,5,[500, 502, 503]).text)[0]
    arr_6=json.loads(get_retry(url_6,5,[500, 502, 503]).text)[0]
    arr_7=json.loads(get_retry(url_7,5,[500, 502, 503]).text)[0]
    arr_8=json.loads(get_retry(url_8,5,[500, 502, 503]).text)[0]

    temp_1=str(arr_1['d1'])
    temp_2=str(arr_2['d1'])
    temp_3=str(arr_3['d1'])
    temp_4=str(arr_4['d1'])
    temp_5=str(arr_5['d1'])
    temp_6=str(arr_6['d1'])
    temp_7=str(arr_7['d1'])
    temp_8=str(arr_8['d1'])

    getdate = datetime.now().strftime('%m月%d日 %H:%M:%S')

    time_1=str(datetime.strptime(arr_1['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_2=str(datetime.strptime(arr_2['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_3=str(datetime.strptime(arr_3['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_4=str(datetime.strptime(arr_4['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_5=str(datetime.strptime(arr_5['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_6=str(datetime.strptime(arr_6['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_7=str(datetime.strptime(arr_7['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    time_8=str(datetime.strptime(arr_8['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')

    tx = open("./txt/temp.html","w",encoding='utf-8')

    tx.write("<style>th{font-size:60px;}td{font-size:80px;font-family:sans-serif; text-align:center;}p{font-size:60px;}</style>")
    tx.write("<table border='1'><tr><th width='450'>センサーNo.</th><th width='400'>現在温度</th></tr>")
    tx.write("<tr><td>No.1</td><td>"+temp_1+" ℃</td></tr>")
    tx.write("<tr><td>No.2</td><td>"+temp_2+" ℃</td></tr>")
    tx.write("<tr><td>No.3</td><td>"+temp_3+" ℃</td></tr>")
    tx.write("<tr><td>No.4</td><td>"+temp_4+" ℃</td></tr>")
    tx.write("<tr><td>No.5</td><td>"+temp_5+" ℃</td></tr>")
    tx.write("<tr><td>No.6</td><td>"+temp_6+" ℃</td></tr>")
    tx.write("<tr><td>No.7</td><td>"+temp_7+" ℃</td></tr>")
    tx.write("<tr><td>No.8</td><td>"+temp_8+" ℃</td></tr></table>")
    tx.write("<p>取得日時:"+getdate+"</p>")

    tx.close()

    sbt = open('./txt/temp_sub.html','w',encoding='utf-8')

    sbt.write('<style> th{ font-size:30px;} td{font-size:30px; font-family:sans-serif;} p{font-size:30px;}</style>')
    sbt.write("<table border='1'><tr><th width='150'>No.</th><th width='200'>最高</th><th width='200'>最低</th><th width='400'>最終取得</th></tr>")
    sbt.write("<tr><td>No.1</td><td></td><td></td><td>"+time_1+"</td></tr>")
    sbt.write("<tr><td>No.2</td><td></td><td></td><td>"+time_2+"</td></tr>")
    sbt.write("<tr><td>No.3</td><td></td><td></td><td>"+time_3+"</td></tr>")
    sbt.write("<tr><td>No.4</td><td></td><td></td><td>"+time_4+"</td></tr>")
    sbt.write("<tr><td>No.5</td><td></td><td></td><td>"+time_5+"</td></tr>")
    sbt.write("<tr><td>No.6</td><td></td><td></td><td>"+time_6+"</td></tr>")
    sbt.write("<tr><td>No.7</td><td></td><td></td><td>"+time_7+"</td></tr>")
    sbt.write("<tr><td>No.8</td><td></td><td></td><td>"+time_8+"</td></tr>")
    sbt.write("<p>取得日時:"+getdate+"</p>")

    sbt.close()

    print("Success. Date:"+getdate)

    time.sleep(30)
