# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:14:35 2023

@author: winni
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/koko-icash/")
tag_div = driver.find_element(By.XPATH,'/html/body/div[1]/main/article/section[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]')
print(tag_div.text)
