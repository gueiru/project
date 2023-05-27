# 進度：可以滑到此網址最底部的頁面，爬取所有文章內容(尚未包含需點擊「顯示更多」後才顯示的內容)



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#以下模擬登入帳號，避免被判爬蟲而鎖IP
# 登入帳號
def login(username, password):
    driver.get("https://www.facebook.com/")
    time.sleep(5)

    # 定位帳號欄位，填入帳號
    username_input = driver.find_element(By.ID, "email")
    username_input.clear()
    username_input.send_keys(username)

    # 定位密碼欄位，填入密碼
    password_input = driver.find_element(By.ID, "pass")
    password_input.clear()
    password_input.send_keys(password)

    # 模擬按下 Enter 鍵登入
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

# 輸入帳號和密碼
username = "winnie910628@gmail.com"
password = "wu020628"

# 登入帳號
login(username, password)
time.sleep(5)

# 進入網頁
driver.get("https://www.facebook.com/groups/442292671308440/")
time.sleep(5)

# 捲動暫停時間
scroll_pause_time = 2  
# 取得初始的捲動高度
scroll_height = driver.execute_script("return document.body.scrollHeight")

# 不斷進行捲動直到頁面底部
while True:
    # 將網頁捲動至底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)  # 暫停一段時間，讓內容載入

    # 將網頁捲動回上方一半的位置
    driver.execute_script("window.scrollBy(0, -window.innerHeight / 2);")
    time.sleep(scroll_pause_time)  # 暫停一段時間，讓內容載入

    # 取得新的捲動高度
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")

    # 比較新舊捲動高度，如果相同代表已經捲動到頁面底部
    if new_scroll_height == scroll_height:
        break

    # 更新捲動高度，繼續進行下一輪捲動
    scroll_height = new_scroll_height

# 定位文章標題
soup = BeautifulSoup(driver.page_source, "lxml")
titles = soup.find_all("div", class_="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a")
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts):
        for post in posts:
            print(post.text)
    print("-" * 20)

driver.quit()
    
    
    


