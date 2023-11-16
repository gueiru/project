import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

url = 'https://www.fubon.com/banking/personal/credit_card/all_card/all_card.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

filtered_card_names = [
    "世界卡", "eTag聯名卡", "現金回饋御璽卡", "雙幣白金卡",
    "台塑聯名卡", "CUBE卡", "蝦皮購物聯名卡", "雙幣商務鈦金卡"
    
    "富邦富利生活系列卡", "富邦數位生活卡", "DHC聯名卡", "福華聯名卡", "富邦無限卡",
    "富邦財神系列卡", "富邦銀行卡", "廣三SOGO悠遊聯名卡", "麗嬰房聯名卡", "OpenPossible聯名卡",
    "富邦Costco聯名卡", "廣三SOGO聯名卡", "台茂聯名卡", "采盟聯名卡", "富邦數位生活悠遊聯名卡",
    "富邦鈦金卡", "富邦數位生活一卡通聯名卡", "富邦IMPERIAL尊御世界卡", "富邦世界卡", "富邦悍將悠遊聯名卡",
    "momo卡", "富邦J卡", "富邦鑽保卡"
    
    "Agoda聯名卡", "Mitsui Shopping Park LaLaport聯名卡", "ALL ME卡",
    "LINE Pay信用卡", "英雄聯盟信用卡", "中油聯名卡",
    "TAIPEI101聯名卡", "和泰聯名卡", "中國信託鼎極卡",
    "中信紅利御璽卡", "中信紅利晶緻卡", "中信現金回饋御璽卡", "中信現金回饋鈦金卡",
    "中信紅利卡", "SuperLife VISA卡",
    "中信兄弟聯名卡", "LEXUS聯名卡", "中信商務卡", "中華電信聯名卡", 
    "漢神百貨聯名卡", "GlobalMall聯名卡",
    "秀泰聯名卡", "大葉髙島屋百貨聯名卡",
    "南紡購物中心聯名卡", "勤美天地聯名卡",
    "MUJI無印良品聯名卡", "酷玩卡", "統一企業認同卡"
]


df = pd.DataFrame(columns=['Keyword', 'Title', 'URL'])

# 設定目標看板
board = 'creditcard'

rows_list = []

# 設定目標看板
board = 'creditcard'

for name in filtered_card_names:
    keyword = str(name)
    target = f"https://www.ptt.cc/bbs/{board}/search?q={keyword}"
    search_response = requests.get(target, headers=headers)
    if search_response.status_code == 200:
        search_soup = BeautifulSoup(search_response.text, 'html.parser')
        articles = search_soup.find_all('div', class_='r-ent')
        for article in articles:
            link = article.find('div', class_='title').a.get('href')
            title = article.find('div', class_='title').text.strip()

            if keyword in title:
                article_url = "https://www.ptt.cc" + link
                article_response = requests.get(article_url, headers=headers)
                article_soup = BeautifulSoup(article_response.text, 'html.parser')
                time_tag = article_soup.find_all('span', class_='article-meta-value')
                published_time_str = time_tag[-1].text if time_tag else 'N/A'

                try:
                    # 轉換成 datetime 格式
                    published_time = datetime.strptime(published_time_str, "%a %b %d %H:%M:%S %Y")

                    # 過濾出 2023 年 9 月以後的資料
                    if published_time >= datetime(2023, 9, 1):
                        rows_list.append({
                            'Keyword': keyword,
                            'Title': title,
                            'URL': article_url,
                            'PublishedTime': published_time
                        })
                except ValueError:
                    # 無法解析日期的情況，你可以在這裡進行處理
                    print(f"無法解析日期: {published_time_str}")
                    
        print("-"*15, f'關鍵字 "{keyword}" 的搜尋結果已獲取完畢，休息一下@@', "-"*15)
        time.sleep(1)
    else:
        print(f'無法取得關鍵字 "{keyword}" 的搜尋結果')

df = pd.DataFrame(rows_list)

# 將整個 DataFrame 寫入 CSV 文件
df.to_csv('cardPTT.csv', index=False, encoding='utf-8-sig')

print("已完成")