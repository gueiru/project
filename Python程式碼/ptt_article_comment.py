import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import pandas as pd

data = pd.DataFrame(columns=['Title', 'ID', "Comment"])

## interview ptt_title_csv【output.csv file】+ url放入list
 # 建立list
url_list = []

 # 開啟CSV檔案
with open('output.csv', 'r', encoding = 'utf-8') as file:
    #  建立CSV讀取器
    reader = csv.reader(file)
    #  讀取CSV檔案的標頭
    header = next(reader)
    #  找到目標欄位的索引
    target_column_index = header.index('URL')
    #  走訪CSV檔案的每一列
    for row in reader:
        #  取得目標欄位(URL)的資料
        target_data = row[target_column_index]
        #  放入list
        url_list.append(target_data)

## 讀取comments
headers = {
    'cookie': 'over18=1',  # 成人驗證碼
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
#  interview ptt_title_csv【output.csv file】+ url放入list
url_list = []

with open('output.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    target_column_index = header.index('URL')

    for row in reader:
        target_data = row[target_column_index]
        url_list.append(target_data)


for url in url_list:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("-" * 30, url, "-" * 30)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('span', class_='article-meta-value').text
        comments = soup.find_all('div', class_='push')

        for comment in comments:
            push_userid = comment.find('span', class_='push-userid').text.strip()
            push_content = comment.find('span', class_='push-content').text.strip()
            new_row = pd.DataFrame({'Title': [title], 'ID': [push_userid], 'Comment': [push_content]})
            data = pd.concat([data, new_row], ignore_index=True)
    else:
        print('無法獲取網頁內容')
time.sleep(3)
data.to_csv('comment.csv', index=False, encoding = 'utf-8-sig')

data = pd.read_csv('comment.csv', encoding='utf-8-sig', delimiter='\t')
print("done processing")
