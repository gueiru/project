# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:43:36 2023

@author: winni
"""

# 顯示更多內容還是無法爬取下來，而且dir="auto"會被重複多爬取一次



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# 使用Selenium打开页面
driver = webdriver.Chrome(ChromeDriverManager().install())

# 模拟登录账号
def login(username, password):
    driver.get("https://www.facebook.com/")
    time.sleep(5)

    # 定位账号栏位，填入账号
    username_input = driver.find_element(By.ID, "email")
    username_input.clear()
    username_input.send_keys(username)

    # 定位密码栏位，填入密码
    password_input = driver.find_element(By.ID, "pass")
    password_input.clear()
    password_input.send_keys(password)

    # 模拟按下 Enter 键登录
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

# 输入账号和密码
username = "xxxx@gmail.com"
password = "xxxx"

# 登录账号
login(username, password)
time.sleep(5)

# 使用Selenium搜索进入目标页面
search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='搜尋 Facebook']")
search_input.send_keys("國泰CUBE好康優惠分享區【非官方】")
search_input.send_keys(Keys.RETURN)
time.sleep(5)

# 点击搜索结果中的目标页面
target_page_link = driver.find_element(By.XPATH, "//a[contains(@href, '/groups/442292671308440/')]")
target_page_link.click()
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

# 定位文章标题
scroll_height = 0
while True:
    # 将页面滚动至底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # 检查是否有“显示更多”的按钮，并点击
    show_more_button = driver.find_element(By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f[role='button']")
    if show_more_button:
        driver.execute_script("arguments[0].click();", show_more_button)
        time.sleep(2)
    else:
        break

    # 获取当前滚动高度
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")

    # 如果滚动高度没有变化，则认为已经滚动到底部
    if new_scroll_height == scroll_height:
        break

    scroll_height = new_scroll_height

# 获取页面内容并解析
soup = BeautifulSoup(driver.page_source, "lxml")
titles = soup.find_all("div", class_=["x78zum5", "xdt5ytf", "xz62fqu", "x16ldp7u"])

# 使用集合存储已经输出的内容
output_set = set()

for title in titles:
    # 将div元素的子元素div[dir='auto']的内容合并
    text_parts = []
    div_auto_elements = title.select("div[dir='auto']")
    for div_auto_element in div_auto_elements:
        text = div_auto_element.text.strip()
        if text:
            text_parts.append(text)

    # 将合并后的内容输出
    merged_text = " ".join(text_parts)
    if merged_text and merged_text not in output_set:
        print(merged_text)
        print("-" * 20)
        output_set.add(merged_text)
