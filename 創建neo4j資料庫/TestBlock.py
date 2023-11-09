from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

# 更改Neo4j Bolt連線設定
uri = "bolt://localhost:7687"
# 這是林宜靜"本地"的neo4j密碼！！！
driver = GraphDatabase.driver(uri, auth=("neo4j", "Test1022"))

# 1. 從Neo4j檢索資料
def retrieve_data(tx):
    query = "MATCH (a)-[r]->(b) RETURN a, r, b"
    result = tx.run(query)
    return list(result)  # 轉換為列表

neo4j_data = []
with driver.session() as session:
    neo4j_data = session.read_transaction(retrieve_data)

# 2. 建立 NetworkX 圖形
G = nx.Graph()

# 以字典的形式记录各个节点的度
node_degrees = {}

for record in neo4j_data:
    # 添加節點
    from_node = record["a"]
    to_node = record["b"]
    G.add_node(from_node.id, label=from_node["name"], category=from_node.labels)
    G.add_node(to_node.id, label=to_node["name"], category=to_node.labels)
    
    # 添加關係
    relation = record["r"]
    G.add_edge(from_node.id, to_node.id, relation=relation.type)

    # 记录节点的度
    node_degrees[from_node.id] = node_degrees.get(from_node.id, 0) + 1
    node_degrees[to_node.id] = node_degrees.get(to_node.id, 0) + 1

# 设置带有 'Categorical' 标签的节点权重为其连接数
for node_id, node_data in G.nodes(data=True):
    if 'Categorical' in node_data['category']:
        node_data['weight'] = node_degrees.get(node_id, 0)

# 3. 繪製圖形（可選）
pos = nx.spring_layout(G)  # 定義節點布局
node_labels = nx.get_node_attributes(G, 'label')
edge_labels = nx.get_edge_attributes(G, 'relation')

weights = nx.get_node_attributes(G, 'weight')

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, node_size=[weights[n] * 100 for n in G.nodes()], node_color='lightblue', font_size=10)
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
