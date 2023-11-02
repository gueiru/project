import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

df = pd.DataFrame(columns=['餐廳', '優惠', '活動期間', '卡片'])

# 設定目標網址
url = "https://www.ctbcbank.com/twrbo/zh_tw/cc_index/cc_offer/cc_offer_food.html"

# 設定 Selenium 瀏覽器
driver = webdriver.Chrome()
driver.get(url)

# 等待 JavaScript 載入完成
time.sleep(5)

# 找到所有優惠資訊
offers = driver.find_elements_by_css_selector("div.twrbo-l-productCard__text")

# 爬取所有頁面資訊
for offer in offers:
    # 取得餐廳名稱
    title = offer.find_element_by_css_selector("div.twrbo-h-margin-bottom-md span.ng-binding").text.strip()

    # 取得優惠內容
    description = offer.find_element_by_css_selector("div.twrbo-l-productTextCard__detail span.ng-binding").text.strip()

    # 取得活動期間
    start_day = offer.find_element_by_css_selector("div.twrbo-c-additionalicon span.ng-binding").text.strip()
    end_day = offer.find_element_by_css_selector("div.twrbo-c-additionalicon span.ng-binding").text.strip()

    # 取得適用卡片
    card_type = offer.find_element_by_css_selector("div.twrbo-c-additionalicon span.ng-scope").text.strip()

    # 儲存資訊
    new_row = pd.DataFrame({'餐廳': title, '優惠': description, '活動期間': start_day + "~" + end_day, '卡片': card_type}, index=[0])
    df = df.append(new_row, ignore_index=True)

# 關閉 Selenium 瀏覽器
driver.quit()

# 儲存結果
df.to_csv('ctbc_food_offers.csv', index=False, encoding='utf-8-sig')

print("已完成")
