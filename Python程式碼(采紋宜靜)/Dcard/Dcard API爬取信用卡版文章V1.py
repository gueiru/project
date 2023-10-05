# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:00:44 2023

@author: winni
"""
# =============================================================================
# # 測試：尚未成功
# import time
# import requests
# import json
# import pandas as pd
# 
# dcard_article = pd.read_csv('Dcard文章資料.csv')
# #https://www.dcard.tw/service/api/v2/posts/235996273/comments?after=60 
# alldata = []
# for articleID in dcard_article['文章ID']:
#     last_comment = ''
#     url = 'https://www.dcard.tw/service/api/v2/posts/'+ str(articleID) +'/comments'
#     doit = True
#     i=0
#     while doit:
#         if i != 0: # 判斷是否是第一次執行
#             request_url = url +'?after='+ str(last_comment)
#         else:
#             request_url = url # 第一次執行，不須加上後方的before
#         list_req = requests.get(request_url) # 請求
#         #將整個網站的程式碼爬下來
#         getdata = json.loads(list_req.content)
#         if len(getdata) > 0:
#             alldata.extend(getdata) # 將另一個陣列插在最後面
#         else:
#             doit = False
#         
#         last_comment = str(len(alldata)) # 取出最後一篇文章
#         print(i)
#         time.sleep(5)
#         i=i+1
#         
# alldata = pd.DataFrame(alldata)
# #翻譯欄位
# alldata.rename(columns={
#     'id':'發文ID',
#     'anonymous':'',
#     'postId':'文章ID',
#     'createdAt':'發文時間',
#     'updateAt':'更新時間',
#     'floor':'樓層',
#     'content':'留言內容',
#     'likeCount':'按讚數',
#     'hiddenByAuthor':'是否被作者隱藏',
#     'gender':'性別',
#     'school':'學校',
#     'host':'是否為發文者',
#     'hidden':'是否隱藏',
#     'department':'個人主頁',
#     }, inplace =True )
# =============================================================================

# =============================================================================
# #存檔
# alldata.to_csv(
#     'Dcard留言資料.csv',      # 檔案名稱
#     encoding = 'utf-8-sig',  # 編碼
#     index = False            # 是否保留index
#     )
# 
# =============================================================================


# =============================================================================
# #無法爬取
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# 
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# 
# time.sleep(5)
# # 進入dcard國泰網頁
# driver.get("https://www.dcard.tw/search?query=%E5%9C%8B%E6%B3%B0&forum=creditcard")
# time.sleep(5)
# 
# for x in range(3):
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     print("scroll")
#     time.sleep(5)
# 
# # 取得頁面內容
# soup = BeautifulSoup(driver.page_source, "html.parser")
# 
# # 尋找連結和文字內容
# links = soup.find_all("a", class_="atm_cs_1urozh atm_c8_1csq7v7 atm_g3_1qqjw7d atm_7l_1pday2 atm_1938jqx_1yyfdc7 atm_2zt8x3_stnw88 atm_grwvqw_gknzbh atm_1ymp90q_idpfg4 atm_89ifzh_idpfg4 atm_1hh4tvs_1osqo2v atm_1054lsl_1osqo2v t1gihpsa")
# 
# for link in links:
#     href = link["href"]
#     full_link = "https://www.dcard.tw" + href
# 
#     driver.get(full_link)
#     time.sleep(2)  # 等待頁面加載
# 
#     soup = BeautifulSoup(driver.page_source, "html.parser")
# 
#     spans = soup.find_all("span")
#     for span in spans:
#         if any(keyword in span.text for keyword in ["中國信託", "中信", "國泰", "國泰世華", "富邦", "台北富邦"]):
#             print(span.text)
# 
# # 關閉瀏覽器
# driver.quit()
# =============================================================================


#無法連線，目標電腦拒絕連線
import time
import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 設定 Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 設定等待時間
WAIT_TIME = 5

# 進行機器人驗證
driver.get("https://www.dcard.tw/service/api/v2/posts/235996273/comments?after=60")
time.sleep(WAIT_TIME)

# 關閉瀏覽器
driver.quit()

# 爬取 API 資料
alldata = []
last_article = ''
for i in range(5):
    if i != 0:  # 判斷是否第一次執行
        requests_url = driver.current_url + '&before=' + str(last_article)
    else:
        requests_url = driver.current_url  # 第一次執行，不須加上後方before

    list_req = requests.get(requests_url)  #請求
    #將整個網站的程式碼爬下來
    getdata = json.loads(list_req.content)
    alldata.extend(getdata)  #將另一個陣列插在最後面
    
    last_article = getdata[-1]['id']  #取出最後一篇文章
    print(last_article)
    time.sleep(10)

alldata = pd.DataFrame(alldata)
# 翻譯欄位
alldata.rename(columns={
    'id': '文章ID',
    'tittle': '標題',
    'excerpt': '內文簡介',
    'anonymousSchool': '學校匿名',
    'anonymousDepartment': '個人主頁',
    'forumId': '版ID',
    'replyId': '回應的文章ID',
    'createdAt': '發文時間',
    'updateAt': '更新時間',
    'commentCount': '回覆數',
    'likeCount': '按讚數',
    'topics': '主題標籤',
    'forumName': '版中文名',
    'forumAlias': '版英文名',
    'gender': '作者性別',
    'school': '作者學校',
    'replyTittle': '回應的文章的標題',
    'layout': '頁面版型',
    'withImages': '是否使用圖片',
    'withVideos': '是否使用影片',
    'media': '媒體連結',
    'department': '個人主頁',
    'categories': '類別',
    'link': '連結(版型為連結才有)',
}, inplace=True)

# =============================================================================
# #存檔
# alldata.to_csv(
#     'Dcard文章標題.csv',  #檔案名稱
#     encoding = 'utf-8-sig',  #編碼
#     index = False  #是否保留index
#     )
# =============================================================================













