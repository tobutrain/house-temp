# -*- coding: utf-8 -*-
import json
import time
import requests
from datetime import datetime
import csv

url = ['http://ambidata.io/api/v2/channels/45860/data?&readKey=9a5d4da14c1c1748&n=1',
    'http://ambidata.io/api/v2/channels/45861/data?&readKey=bf91b4b4953bb597&n=1',
    'http://ambidata.io/api/v2/channels/45862/data?&readKey=3931de126d84d265&n=1',
    'http://ambidata.io/api/v2/channels/45863/data?&readKey=7928fdfe2bc2a3cf&n=1',
    'http://ambidata.io/api/v2/channels/45864/data?&readKey=fb85ec6edc5e82d6&n=1',
    'http://ambidata.io/api/v2/channels/45865/data?&readKey=b91097b4ee8f7320&n=1',
    'http://ambidata.io/api/v2/channels/45866/data?&readKey=8e40f5bc024aedd9&n=1',
    'http://ambidata.io/api/v2/channels/45867/data?&readKey=269393e563d71a55&n=1']

file_mainhtml='/var/www/temp-hase.info/txt/temp.html'
file_subhtml='/var/www/temp-hase.info/txt/temp_sub.html'
file_csv='/var/www/temp-hase.info/txt/hl.csv'

#定義 URLから情報が取得できなかった場合に再試行する
def get_retry(url, retry_times, errs):
    for t in range(retry_times + 1):
        r = requests.get(url)
        if t < retry_times:
            if r.status_code in errs:
                time.sleep(5)
                continue
        return r

#CSV繝輔ぃ繧､繝ｫ繧帝幕縺?縺ｦ?ｼ碁?榊?励ｒ繝ｪ繧ｹ繝亥??蛹?陦ｨ險倥〒蜿悶ｊ蜃ｺ縺?
#蜀?蛹?繝?繝ｼ繧ｿ繧貞叙繧雁?ｺ縺呎凾縺ｯ?ｼ慶sv_hl[繧ｻ繝ｳ繧ｵNo][h:0,l:1]
with open(file_csv,encoding="utf-8") as cf:
    cfrd = csv.reader(cf)
    csv_hl=[row for row in cfrd]

#譛�鬮俶ｸｩ蠎ｦ縺ｨ譛�菴取ｸｩ蠎ｦ繧剃ｻ｣蜈･縺吶ｋ

high = []

for i in range(7):
    high[i] = csv_hl[i][0]
h1=csv_hl[0][0]
h2=csv_hl[1][0]
h3=csv_hl[2][0]
h4=csv_hl[3][0]
h5=csv_hl[4][0]
h6=csv_hl[5][0]
h7=csv_hl[6][0]
h8=csv_hl[7][0]

l1=csv_hl[0][1]
l2=csv_hl[1][1]
l3=csv_hl[2][1]
l4=csv_hl[3][1]
l5=csv_hl[4][1]
l6=csv_hl[5][1]
l7=csv_hl[6][1]
l8=csv_hl[7][1]

#譛�鬮假ｼ乗怙菴取ｰ玲ｸｩ繝ｪ繧ｹ繝?
hi_lst=[h1,h2,h3,h4,h5,h6,h7,h8]
lo_lst=[l1,l2,l3,l4,l5,l6,l7,l8]

#Ambient縺九ｉ?ｼ後そ繝ｳ繧ｵ貂ｬ螳壽ｰ玲ｸｩ繧貞叙蠕?
arr_1=json.loads(get_retry(url_1,6,[500, 502, 503]).text)[0]
arr_2=json.loads(get_retry(url_2,6,[500, 502, 503]).text)[0]
arr_3=json.loads(get_retry(url_3,6,[500, 502, 503]).text)[0]
arr_4=json.loads(get_retry(url_4,6,[500, 502, 503]).text)[0]
arr_5=json.loads(get_retry(url_5,6,[500, 502, 503]).text)[0]
arr_6=json.loads(get_retry(url_6,6,[500, 502, 503]).text)[0]
arr_7=json.loads(get_retry(url_7,6,[500, 502, 503]).text)[0]
arr_8=json.loads(get_retry(url_8,6,[500, 502, 503]).text)[0]

temp_1=str(arr_1['d1'])
temp_2=str(arr_2['d1'])
temp_3=str(arr_3['d1'])
temp_4=str(arr_4['d1'])
temp_5=str(arr_5['d1'])
temp_6=str(arr_6['d1'])
temp_7=str(arr_7['d1'])
temp_8=str(arr_8['d1'])

#迴ｾ蝨ｨ豌玲ｸｩ繝ｪ繧ｹ繝?
temp_lst=[temp_1,temp_2,temp_3,temp_4,temp_5,temp_6,temp_7,temp_8]

#Ambient縺九ｉ?ｼ後そ繝ｳ繧ｵ豌玲ｸｩ貂ｬ螳壽凾蛻ｻ繧貞叙蠕?
time_1=str(datetime.strptime(arr_1['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_2=str(datetime.strptime(arr_2['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_3=str(datetime.strptime(arr_3['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_4=str(datetime.strptime(arr_4['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_5=str(datetime.strptime(arr_5['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_6=str(datetime.strptime(arr_6['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_7=str(datetime.strptime(arr_7['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
time_8=str(datetime.strptime(arr_8['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')

#迴ｾ蝨ｨ譎ょ綾繧貞叙蠕?
getdate = datetime.now().strftime('%m譛?%d譌･ %H:%M:%S')

#迴ｾ蝨ｨ豌玲ｸｩ縺ｨ譛�菴趣ｼ梧怙鬮俶ｰ玲ｸｩ繧呈ｯ碑ｼ?(譛�鬮俶ｰ玲ｸｩ?ｼ梧怙菴取ｰ玲ｸｩ繧呈峩譁ｰ)
for num_comhi in range(0,8):
    if float(temp_lst[num_comhi])>float(hi_lst[num_comhi]):
        hi_lst[num_comhi]=float(temp_lst[num_comhi])

for num_comlo in range(0,8):
    if float(temp_lst[num_comlo])<float(lo_lst[num_comlo]):
        lo_lst[num_comlo]=float(temp_lst[num_comlo])

#HTML譖ｸ縺崎ｾｼ縺ｿ
tx = open(file_mainhtml,"w",encoding='utf-8')

tx.write("<style>th{font-size:60px;}td{font-size:80px;font-family:sans-serif; text-align:center;}p{font-size:60px;}</style>")
tx.write("<table border='1'><tr><th width='450'>繧ｻ繝ｳ繧ｵ繝ｼNo.</th><th width='400'>迴ｾ蝨ｨ貂ｩ蠎ｦ</th></tr>")
tx.write("<tr><td>No.1</td><td>"+temp_1+" 邃?</td></tr>")
tx.write("<tr><td>No.2</td><td>"+temp_2+" 邃?</td></tr>")
tx.write("<tr><td>No.3</td><td>"+temp_3+" 邃?</td></tr>")
tx.write("<tr><td>No.4</td><td>"+temp_4+" 邃?</td></tr>")
tx.write("<tr><td>No.5</td><td>"+temp_5+" 邃?</td></tr>")
tx.write("<tr><td>No.6</td><td>"+temp_6+" 邃?</td></tr>")
tx.write("<tr><td>No.7</td><td>"+temp_7+" 邃?</td></tr>")
tx.write("<tr><td>No.8</td><td>"+temp_8+" 邃?</td></tr></table>")
tx.write("<p>蜿門ｾ玲律譎?:"+getdate+"</p>")

tx.close()

sbt = open(file_subhtml,'w',encoding='utf-8')

sbt.write('<style> th{ font-size:40px;} td{font-size:45px; font-family:sans-serif;} p{font-size:30px;}</style>')
sbt.write("<table border='1'><tr><th width='120'>No.</th><th width='120'>譛�鬮?</th><th width='120'>譛�菴?</th><th width='450'>譛�邨ょ叙蠕?</th></tr>")
sbt.write("<tr><td>No.1</td><td>"+h1+"</td><td>"+l1+"</td><td>"+time_1+"</td></tr>")
sbt.write("<tr><td>No.2</td><td>"+h2+"</td><td>"+l2+"</td><td>"+time_2+"</td></tr>")
sbt.write("<tr><td>No.3</td><td>"+h3+"</td><td>"+l3+"</td><td>"+time_3+"</td></tr>")
sbt.write("<tr><td>No.4</td><td>"+h4+"</td><td>"+l4+"</td><td>"+time_4+"</td></tr>")
sbt.write("<tr><td>No.5</td><td>"+h5+"</td><td>"+l5+"</td><td>"+time_5+"</td></tr>")
sbt.write("<tr><td>No.6</td><td>"+h6+"</td><td>"+l6+"</td><td>"+time_6+"</td></tr>")
sbt.write("<tr><td>No.7</td><td>"+h7+"</td><td>"+l7+"</td><td>"+time_7+"</td></tr>")
sbt.write("<tr><td>No.8</td><td>"+h8+"</td><td>"+l8+"</td><td>"+time_8+"</td></tr>")
sbt.write("<p>蜿門ｾ玲律譎?:"+getdate+"</p>")

sbt.close()

#CSV譖ｸ縺崎ｾｼ縺ｿ
wcsv = open(file_csv,'w',encoding="utf-8",newline='')
writer=csv.writer(wcsv)
for num_wr in range(0,8):
    writer.writerow((str(hi_lst[num_wr]),str(lo_lst[num_wr])))

wcsv.close()

#鬮俶ｸｩ譎?,LINE縺ｫ騾夂衍縺吶ｋ

def send_line_notify(notification_message):
    line_notify_token = 'UmQClQJvwC2MTnP3pTdl0iX3nL8Esi2XWURU7MI6lnb'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)


temp_max = float(max(temp_lst))
#idx = int(temp_lst.index(temp_max))
notify_temp = float(35)
if temp_max>=notify_temp:
    send_line_notify("貂ｩ蠎ｦ縺御ｸ頑??縺励※縺?縺ｾ縺呻ｼ? 貂ｩ蠎ｦ:"+str(temp_max)+"邃?")

print("Success. Date:"+getdate)
