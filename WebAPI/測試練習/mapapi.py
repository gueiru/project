import requests
import json

# 設定 Google Maps API 金鑰
API_KEY = "打碼打碼API_KEY"

# 設定查詢經緯度
LATITUDE = 37.7752
LONGITUDE = -122.4188

# 建立 Google Maps API 查詢物件
params = {
    "key": API_KEY,
    "location": f"{LATITUDE},{LONGITUDE}",
    "radius": 5000,
    "type": "store|restaurant"
}

# 發送查詢請求
response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params)

# 解析查詢回應
results = json.loads(response.content)

# 列出距離最近的五個銷售店家
for result in results["results"]:
    print(f"名稱：{result['name']}")
    
from flask import Flask, request

# 建立一個 Flask 應用程式
app = Flask(__name__)

# 建立一個路由，用於處理查詢請求
@app.route("/nearby_stores", methods=["GET"])
def nearby_stores():
    # 從請求中取得經緯度
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    # 建立 Google Maps API 查詢物件
    params = {
        "key": API_KEY,
        "location": f"{latitude},{longitude}",
        "radius": 5000,
        "type": "store"
    }

    # 發送查詢請求
    response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params)

    # 解析查詢回應
    results = json.loads(response.content)

    # 列出距離最近的五家銷售店家
    for result in results["results"]:
        return jsonify({
            "name": result["name"],
        })

# 啟動應用程式
if __name__ == "__main__":
    app.run(debug=True)

