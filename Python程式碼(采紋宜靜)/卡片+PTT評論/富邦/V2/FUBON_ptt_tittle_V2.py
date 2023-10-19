# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:18:57 2023

@author: winni
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

df = pd.DataFrame(columns=['Keyword', 'Title', 'URL'])

# 設定目標看板和關鍵字
board = 'creditcard'
keywords = ["富邦J卡", "富邦IMPERIAL尊御世界卡", "富邦數位生活卡", "富邦鑽保卡", "富邦財神系列卡", "Open Possible聯名卡", "富邦世界卡" ,"富邦無限卡", "富邦富利生活系列卡", "富邦鈦金卡",  "富邦銀行卡", "富邦Costco聯名卡", "momo卡", "富邦悍將悠遊聯名卡", "台茂聯名卡", "廣三SOGO聯名卡", "采盟聯名卡", "DHC聯名卡", "福華聯名卡", "麗嬰房聯名卡", "富邦商務卡"]

# 設定PTT需要的Headers
headers = {
    'cookie': 'over18=1',  # 成人驗證
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

for keyword in keywords:
    target = f"https://www.ptt.cc/bbs/{board}/search?q={keyword}"
    search_response = requests.get(target, headers=headers)
    if search_response.status_code == 200:
        search_soup = BeautifulSoup(search_response.text, 'html.parser')
        articles = search_soup.find_all('div', class_='r-ent')
        # 逐一處理文章
        for article in articles:
            # 取得文章連結
            link = article.find('div', class_='title').a.get('href')
            # get title
            title = article.find('div', class_='title').text.strip()
            if keyword in title:
                article_url = "https://www.ptt.cc" + link
                new_row = pd.DataFrame({'Keyword': keyword, 'Title': title, 'URL': article_url}, index=[0])
                df = pd.concat([df, new_row], ignore_index=True)
        print("-"*15, f'關鍵字 "{keyword}" 的搜尋結果已獲取完畢，休息一下@@', "-"*15)
        time.sleep(3)
    else:
        print(f'無法取得關鍵字 "{keyword}" 的搜尋結果')

df.to_csv('FUBON_ptt_tittle_V2.csv', index=False, encoding = 'utf-8-sig')
print("已完成")


