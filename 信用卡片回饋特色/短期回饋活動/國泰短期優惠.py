import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cathaybk.com.tw/cathaybk/personal/event/overview/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    df = pd.DataFrame(columns=['Title', 'Text', 'Date'])
    
    # 短期活動
    event_cards = soup.find_all('div', class_='cubre-m-eventCard__content')
    for event_card in event_cards:
        title = event_card.find('div', class_='cubre-m-eventCard__title').text
        text = event_card.find('div', class_='cubre-m-eventCard__text').text
        date_elem = event_card.find('div', class_='cubre-m-eventCard__date')
        date = date_elem.text if date_elem else None  # 如果找不到日期元素，则将 date 设为 None

        # data to DataFrame
        new_row = pd.DataFrame({'Title': [title], 'Text': [text], 'Date': [date]})
        df = pd.concat([df, new_row], ignore_index=True)
        
else:
    print("get error：", response.status_code)

df.to_csv('國泰短期優惠.csv', index=False, encoding='utf-8-sig')
print("CSV file has been created.")