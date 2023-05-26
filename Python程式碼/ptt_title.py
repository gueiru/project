import requests
from bs4 import BeautifulSoup

# 設定目標看板和關鍵字
board = 'creditcard'
keywords = ["中信", "cube", "富邦"]

# 設定PTT需要的Headers
headers = {
    'cookie': 'over18=1',  # 成人驗證
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# 發送GET請求
url = f'https://www.ptt.cc/bbs/{board}/index.html'
response = requests.get(url, headers=headers)

# 檢查請求是否成功
if response.status_code == 200:
    # 解析HTML內容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for keyword in keywords:
        target = f"https://www.ptt.cc/bbs/{board}/search?q={keyword}"
        articles = soup.find_all('div', class_='r-ent')
        # 逐一處理文章
        for article in articles:
            # 取得文章連結
            link = article.find('div', class_='title').a.get('href')
            # get title
            title = article.find('div', class_='title').text.strip()
            if keyword in title:
                article_url = "https://www.ptt.cc" + link
                print(title)
                print(article_url)
        
        print("-" * 30)
                
else:
    print('無法取得網頁內容')
