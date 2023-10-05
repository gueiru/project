from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

#更改Neo4j Bolt連線設定
uri = "bolt://localhost:7687"
#這是林宜靜"本地"的neo4j密碼！！！
driver = GraphDatabase.driver(uri, auth=("neo4j", "Password0422"))

def do_Cypher(tx, text):
    result = tx.run(text)
    return result

#建立節點函式
def create_knowledge_point(tx, obj, relation, label):
    command = []
    # 查看 node A 是否存在
    text = "MATCH (n:"+label+" {name: '"+obj+"'}) RETURN n"
    result = tx.run(text)
    # 檢查查詢結果
    if not result.peek():
        # 如果節點不存在，則建立它
        text = "CREATE ("+obj+":"+label+" {name: '"+obj+"'})"
        tx.run(text)
        command.append(text)
        print("Node created.")
    else:
        print("Node already exists.")
    print(command)
    
    # 查看 node B 是否存在
    text = "MATCH (n:Categorical {name: '"+label+"'}) RETURN n"
    result = tx.run(text)    
    # 檢查查詢結果
    if not result.peek():
        # 如果節點不存在，則建立它
        text = "CREATE ("+label+":Categorical {name: '"+label+"'})"
        tx.run(text)
        command.append(text)
        print("Node created.")
    else:
        print("Node already exists.")
    print(command)
    
    # 查看 node A 與 node B 之間的關係是否存在
    text = "MATCH (a:"+label+" {name: '"+obj+"'}), (b:Categorical {name: '"+label+"'}) RETURN EXISTS((a)-[:"+relation+"]->(b)) AS relationship_exists"
    result = tx.run(text)
    single_result = result.single()
    if single_result is not None:
        exists = single_result["relationship_exists"]
    else:
        exists = False
    
    # 如果關聯不存在，則建立它
    if exists is False:
        text = "MATCH (a:"+label+" {name: '"+obj+"'}), (b:Categorical {name: '"+label+"'}) CREATE (a)-[:"+relation+"]->(b)"
        tx.run(text)
        command.append(text)
        print("Relationship created.")
    else:
        print("Relationship already exists.")
    
    print(command)

# 國泰卡片
with driver.session() as session:
    card = ['CUBE卡', '台塑聯名卡', '世界卡', '現金回饋御璽卡', '蝦皮購物聯名卡', 'eTag聯名卡', '雙幣卡', '亞洲萬里通聯名里享卡', '長榮聯名御璽卡', '亞洲萬里通聯名白金卡', '長榮聯名極致御璽卡', '亞洲萬里通聯名鈦商卡']
    for card in card:
        session.write_transaction(create_knowledge_point, card, "is", "國泰信用卡")

# 影音串流平台匯入區
with driver.session() as session:
    music = ["Google_Play", "Disney_Plus", "Netflix", "Spotify", "KKBOX", "KKTV"]
    for music in music:
        session.write_transaction(create_knowledge_point, music, "is", "串流平台")

#電商平台匯入區
with driver.session() as session:
    shopping_websites = ["蝦皮購物", "momo購物網", "PChome線上購物", "Yahoo奇摩購物中心", "小樹購"]
    for shop in shopping_websites:
        session.write_transaction(create_knowledge_point, shop, "is", "電商")
