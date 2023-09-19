import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import pandas as pd

data = pd.DataFrame(columns=['Title', 'ID', 'Comment'])

url_list = []

with open('國泰card_PttURL.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    target_column_index = header.index('URL')
    for row in reader:
        target_data = row[target_column_index]
        url_list.append(target_data)

# 设置请求头
headers = {
    'cookie': 'over18=1',  
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

data = pd.DataFrame(columns=['Title', 'ID', 'Comment'])

for url in url_list:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("-" * 30, url, "-" * 30)
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            title = soup.find('span', class_='article-meta-value').text
        except AttributeError:
            print("no tilte:", url)
            continue  # 跳過沒有標題的貼文

        comments = soup.find_all('div', class_='push')

        for comment in comments:
            push_userid = comment.find('span', class_='push-userid').text.strip()
            push_content = comment.find('span', class_='push-content').text.strip()
            new_row = pd.DataFrame({'Title': [title], 'ID': [push_userid], 'Comment': [push_content]})
            data = pd.concat([data, new_row], ignore_index=True)
    else:
        print('error:', url)
time.sleep(3)

data.to_csv('國泰comment.csv', index=False, encoding='utf-8-sig')

data = pd.read_csv('國泰comment.csv', encoding='utf-8-sig', delimiter=',')
print("done processing")
