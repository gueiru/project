from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

#更改Neo4j Bolt連線設定
uri = "neo4j+s://cd122923.databases.neo4j.io "
driver = GraphDatabase.driver(uri, auth=("neo4j", "XMvLaxouvDASwAcmMpcndl7W9j6pf6RpLs7ahPjjxQg"))

def do_Cypher(tx, text):
    result = tx.run(text)
    return result

#建立節點函式
def create_relationship(tx, from_node_name, to_node_names, relation_type):
    # 查詢並建立關聯
    query = (
        "MATCH (from_node {name: $from_node_name}) "
        "MATCH (to_nodes) WHERE to_nodes.name IN $to_node_names "
        "WITH from_node, COLLECT(to_nodes) AS targets "
        "FOREACH (target IN targets | CREATE (from_node)-[r:" + relation_type + "]->(target))"
    )

    tx.run(query, from_node_name=from_node_name, to_node_names=to_node_names)

#-------------------------------以下為建立資料庫的 code------------------------------------------
  
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