import requests
from bs4 import BeautifulSoup

def get_globalmall_discounts():
    # 取得 GlobalMall 官網的優惠資訊
    url = "https://www.globalmall.com.tw/promotions"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 提取 GlobalMall 聯名卡的優惠資訊
    discounts = []
    for card in soup.find_all("div", class_="card-discount"):
        title = card.find("h2").text
        description = card.find("p").text
        discounts.append({
            "title": title,
            "description": description
        })

    return discounts

def main():
    discounts = get_globalmall_discounts()

    # 輸出優惠資訊
    for discount in discounts:
        print(discount["title"])
        print(discount["description"])

if __name__ == "__main__":
    main()