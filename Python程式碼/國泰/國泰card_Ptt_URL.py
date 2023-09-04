import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

#國泰卡片
url = 'https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding="UTF-8")

    
    card_elements = soup.find_all('div', class_='cubre-m-compareCard__title')
    card_names = [card.text for card in card_elements]
    
    # 移除不是"卡"字元結尾和"金融卡"結尾的項目
    filtered_card_names = [card for card in card_names if card.endswith("卡") and not card.endswith("金融卡")]
    
    
    #Use "set" to remove duplicates
    print(list(set(filtered_card_names)))
    print()
    print(len(list(set(filtered_card_names))))
else:
    print("Failed to retrieve the webpage.")



df = pd.DataFrame(columns=['Keyword', 'Title', 'URL'])

# 設定目標看板
board = 'creditcard'

for name in filtered_card_names:
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