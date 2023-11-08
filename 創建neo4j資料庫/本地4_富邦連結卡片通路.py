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
# eTag聯名卡
with driver.session() as session:
    rewards = [
        "馥蘭朵烏來渡假酒店", "馥蘭朵墾丁渡假酒店", "台南遠東香格里拉"
    ]   


print("-------------done----------")
