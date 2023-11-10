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
keywords = ["Agoda聯名卡", "Mitsui Shopping Park LaLaport聯名卡", "中華航空聯名卡", "ALL ME卡", "LINE Pay信用卡", "英雄聯盟信用卡", "中油聯名卡" ,"中信商旅鈦金卡", "TAIPEI 101 聯名卡", "和泰聯名卡",  "中國信託鼎極卡", "中信紅利御璽卡", "中信紅利晶緻卡", "中信現金回饋御璽卡", "中信現金回饋鈦金卡", "中信紅利卡", "寰遊美國運通卡", "iPlan卡", "Super Life VISA卡", "ANA聯名卡", "中信兄弟聯名卡",  "LEXUS聯名卡", "中信商務卡/雙幣商務卡", "中華電信聯名卡", "漢神百貨聯名卡", "Global Mall聯名卡", "秀泰聯名卡", "大葉髙島屋百貨聯名卡", "南紡購物中心聯名卡", "勤美天地聯名卡", "MUJI無印良品聯名卡", "酷玩卡", "統一企業認同卡"]

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

df.to_csv('CTBC_ptt_tittle_V2.csv', index=False, encoding = 'utf-8-sig')
print("已完成")


