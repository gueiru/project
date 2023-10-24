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

print("-------------done----------")