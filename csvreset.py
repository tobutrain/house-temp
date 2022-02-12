import csv
import json
import requests
import time

url_1='http://ambidata.io/api/v2/channels/45860/data?&readKey=9a5d4da14c1c1748&n=1'
url_2='http://ambidata.io/api/v2/channels/45861/data?&readKey=bf91b4b4953bb597&n=1'
url_3='http://ambidata.io/api/v2/channels/45862/data?&readKey=3931de126d84d265&n=1'
url_4='http://ambidata.io/api/v2/channels/45863/data?&readKey=7928fdfe2bc2a3cf&n=1'
url_5='http://ambidata.io/api/v2/channels/45864/data?&readKey=fb85ec6edc5e82d6&n=1'
url_6='http://ambidata.io/api/v2/channels/45865/data?&readKey=b91097b4ee8f7320&n=1'
url_7='http://ambidata.io/api/v2/channels/45866/data?&readKey=8e40f5bc024aedd9&n=1'
url_8='http://ambidata.io/api/v2/channels/45867/data?&readKey=269393e563d71a55&n=1'

file_csv='/var/www/temp-hase.info/txt/hl.csv'

#定義 get_retry HTTPgetが正常終了しなかった時に2秒後再取得する(retry_times回繰り返す)
def get_retry(url, retry_times, errs):
    for t in range(retry_times + 1):
        r = requests.get(url)
        if t < retry_times:
            if r.status_code in errs:
                time.sleep(2)
                continue
        return r

#Ambientから，センサ測定気温を取得
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

#現在気温リスト
temp_lst=[temp_1,temp_2,temp_3,temp_4,temp_5,temp_6,temp_7,temp_8]

hi_lst=[]
lo_lst=[]

for num_comhi in range(8):
    hi_lst.append(temp_lst[num_comhi])

for num_comlo in range(8):
    lo_lst.append(temp_lst[num_comlo])

wcsv = open(file_csv,'w',encoding="utf-8",newline='')
writer=csv.writer(wcsv)
for num_wr in range(8):
    writer.writerow((str(hi_lst[num_wr]),str(lo_lst[num_wr])))

wcsv.close()
