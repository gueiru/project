from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

#更改Neo4j Bolt連線設定
uri = "bolt://localhost:7687"
#這是林宜靜"本地"的neo4j密碼！！！
driver = GraphDatabase.driver(uri, auth=("neo4j", "Test1022"))

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
# 富邦富利生活系列卡
with driver.session() as session:
    rewards = [
        "百貨公司", "超市", "國內餐飲", "加油站", "書局",
        "旅行社",
        "虎航", "長榮航空", "華航", "星宇", "立榮",  "華信"
    ]
    session.write_transaction(create_relationship, "富邦富利生活系列卡", rewards, "reward")

# 富邦數位生活卡
with driver.session() as session:
    rewards = [
        "yahoo奇摩購物中心", "yahoo超級商城", "yahoo拍賣", "pchome線上購物",
        "pchome商店街", "淘寶", "天貓", "蝦皮購物",
        "myfone購物", "udn買東西", "樂天", "friday購物", "博客來", "生活市集",
        "松果購物", "citiesocial找好東西", "zalora", "shopback",
        "東森", "森森", "viva", "momo",
        
        "台灣大哥大", "中華電信", "遠傳", "台灣之星", "亞太"
    ]
    session.write_transaction(create_relationship, "富邦數位生活卡", rewards, "reward")

print("-------------done----------")
