from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

#更改Neo4j Bolt連線設定
uri = "neo4j+s://cd122923.databases.neo4j.io "
driver = GraphDatabase.driver(uri, auth=("neo4j", "Password"))

def do_Cypher(tx, text):
    result = tx.run(text)
    return result

#建立節點函式
def create_relationship(tx, from_node_name, to_node_names, relation_type):
    # 使用MERGE來建立關聯，如果關聯已存在，則不會重複建立
    query = (
        "MATCH (from_node {name: $from_node_name}) "
        "UNWIND $to_node_names AS to_node_name "
        "MATCH (to_node {name: to_node_name}) "
        "MERGE (from_node)-[r:" + relation_type + "]->(to_node) "
        "RETURN r"
    )

    result = tx.run(query, from_node_name=from_node_name, to_node_names=to_node_names)
    
    if result.peek():
        print("--Relationship existed--")
    else:
        print("++Relationship created++")


#-------------------------------以下為建立資料庫的 code------------------------------------------
# CUBE卡_慶生月
with driver.session() as session:
    rewards = [
        "遠東SOGO百貨", "太平洋百貨", "廣三SOGO0",
        
        "民宿", "青年旅館", "連鎖飯店",
        
        "茹絲葵經典牛排館", "屋馬燒肉", "solo_pasta義大利麵", 
        "俺達の肉屋_日本和牛專門店", "鹽之華法式餐廳", "廚房有雞花雕雞", "碳佐麻里精品燒肉", 
        "与玥樓頂級粵菜餐廳", "RAW", "山海樓", "金蓬萊遵古台菜餐廳", "老新台菜",
        
        "國賓影城", "威秀影城", "ShowTimes秀泰影城",
        
        "錢櫃KTV", "好樂迪KTV", "星聚點KTV", "享溫馨KTV" 
    ]
    session.write_transaction(create_relationship,"CUBE卡_慶生月", rewards, "reward")
    
# CUBE卡_集精選
with driver.session() as session:
    rewards = [
        "家樂福",
        "台灣中油-直營店",
        "高鐵",
        "SevenEleven", "FamilyMart", "全聯福利中心"
        "麥當勞", "星巴克",
        "foodomo",
        "遠東SOGO百貨",
        "博客來",
        "城市車旅", "嘟嘟房",
        "OPEN錢包"
    ]
    session.write_transaction(create_relationship,"CUBE卡_集精選", rewards, "reward")
    
# CUBE卡_趣旅行
with driver.session() as session:
    rewards = [
        "日本", "韓國", "泰國", "新加坡", "國外餐飲",
               
        "Uber", "LINE_TAXI", "yoxi", "台灣大車隊", "大都會計程車",
        
        "和運租車", "iRent", "格上租車", "中租租車", "AVIS租車",
        
        "飛機",
        
        "民宿", "青年旅館", "連鎖飯店",
        
        "KKday", "Agoda", "KLOOK", "Airbnb", "Hotels_com",
        "Expedia", "Booking_com", "Trip_com", "AsiaYo",
        
        "ezTravel易遊網", "雄獅旅遊",
        "可樂旅遊", "東南旅遊", "五福旅遊", "燦星旅遊", "山富旅遊", "長汎假期",
        "鳳凰旅行社", "Ezfly易飛網", "理想旅遊", "永利旅行社", "三賀旅行社"
        ]
    session.write_transaction(create_relationship, "CUBE卡_趣旅行", rewards, "reward")
  
# CUBE卡_玩數位
with driver.session() as session:
    rewards = ["Google_Play", "Disney_Plus", "Netflix", "Spotify", "KKBOX", "KKTV",
        "App_Store", "Apple_Music", "iCloud",
                
        "蝦皮購物", "momo購物網", "PChome線上購物", "Yahoo奇摩購物中心", "小樹購",
        "Amazon", "淘寶", "天貓"]
    session.write_transaction(create_relationship, "CUBE卡_玩數位", rewards, "reward")

# CUBE卡_樂饗購
with driver.session() as session:
    rewards = [ "遠東SOGO百貨", "太平洋百貨", "新光三越", "SKM_Park", "遠東百貨",
                "Big_City遠東巨城購物中心", "微風廣場", "誠品生活", "環球購物中心", "CITYLINK",
                "BELLAVITA", "統一時代", "台北101", "ATT_4_FUN", "明曜百貨", "京站",
                "美麗華", "大葉高島屋", "遠企購物中心", "比漾廣場", "大江國際購物中心",
                "中友百貨", "廣三SOGO", "Tiger_City", "勤美誠品綠園道", "金典綠園道",
                "大魯閣新時代", "耐斯廣場", "南紡購物中心", "德安百貨", "夢時代", "大立百貨",
                "大統百貨", "漢神百貨", "漢神巨蛋", "MITSUI_OUTLET_PARK(林口、台中港、台南)",
                "Mitsui_Shopping_Park_LaLaport(台中)", "禮客", "義大世界購物廣場", "華泰名品城",
                "義享天地", "麗寶OUTLET_Mall", "麗寶百貨廣場", "秀泰生活", "徐匯廣場",
                "台茂購物中心", "桃園統領百貨", "新月廣場", "日曜天地", "三創生活", "_6_Plaza廣場",
                "iFG遠雄廣場", "台南FOCUS", "悅誠廣場", "欣欣百貨", "宏匯廣場",
                "高雄棧貳庫商場", "樂購廣場", "NOKE忠泰樂生活", "昇恆昌", 
                
                "Uber_Eats", "foodpanda", "foodomo", "inline", 
                
                "國內餐飲",
                
                "康是美", "寶雅", "屈臣氏", "日藥本舖", "Tomod_s", "松本清"
            ]
    session.write_transaction(create_relationship, "CUBE卡_樂饗購", rewards, "reward")

print("-------------done----------")
