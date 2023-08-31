import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

#國泰卡片
card = ["CUBE卡", "蝦皮購物聯名卡", "世界卡", "現金回饋御璽卡", "商務卡", "亞洲萬里通聯名卡", "長榮航空聯名卡",
        "台塑聯名卡", "雙幣卡", "eTag聯名卡", "KOKO COMBO icash聯名卡", "KOKO(COMBO)悠遊聯名卡", "KOKO icash聯名卡"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
df = pd.DataFrame(columns=['Keyword', 'Title', 'URL'])

# 設定目標看板
board = 'creditcard'

for name in card:
    keyword = str(name)  # 确保字符串化卡片名稱
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

df.to_csv('國泰card_PttURL.csv', index=False, encoding='utf-8-sig')
print("已完成")