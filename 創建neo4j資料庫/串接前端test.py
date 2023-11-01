from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

# 建立與 Neo4j 的連接
uri = "neo4j+s://cd122923.databases.neo4j.io "
driver = GraphDatabase.driver(uri, auth=("neo4j", "XMvLaxouvDASwAcmMpcndl7W9j6pf6RpLs7ahPjjxQg"))

# 建立連線函式
def connect_to_neo4j(uri, username, password):
    return GraphDatabase.driver(uri, auth=(username, password))

# 定義一個查詢函式
def run_query(driver, query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()

# 例子: 執行一個簡單的查詢
query = "MATCH (n) RETURN n LIMIT 5"

# 執行查詢
result = run_query(driver, query)

# 處理結果
for record in result:
    print(record)
