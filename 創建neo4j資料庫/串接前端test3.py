from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

#更改Neo4j Bolt連線設定
uri = "bolt://localhost:7687"
#這是林宜靜"本地"的neo4j密碼！！！
driver = GraphDatabase.driver(uri, auth=("neo4j", "Test1022"))

def search_nodes_related_to_card(self, input_string):
    query = (
        "MATCH (n:NodeLabel)-[:RELATED_TO]->(c:card) "
        "WHERE n.name CONTAINS $input_string "
        "RETURN n, c"
    )

    with self._driver.session() as session:
        result = session.run(query, input_string=input_string)
        return result.data()



input_string = "全家"
with driver.session() as session:
    result_data = session.read_transaction(search_nodes_related_to_card, input_string)

# 處理查詢結果
for record in result_data:
    print(record)

# 關閉 Neo4j 連線
driver.close()