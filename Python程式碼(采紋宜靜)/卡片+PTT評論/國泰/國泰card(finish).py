import requests
from bs4 import BeautifulSoup
import csv

#國泰官網
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
