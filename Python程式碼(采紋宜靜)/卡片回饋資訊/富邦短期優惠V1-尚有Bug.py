import requests
from bs4 import BeautifulSoup
import re

url = "https://creditcard.taipeifubon.com.tw/promo/food/index.jsp"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a", class_="clearfix", style="cursor:pointer", onclick=re.compile("goDetails\((.*?)\)"))

# 將 element 存到陣列裡
if links:
    promotions = []
    for link in links:
        promotions.append(link["onclick"].split("(")[1].split(")", 1)[0])

    print(promotions)
