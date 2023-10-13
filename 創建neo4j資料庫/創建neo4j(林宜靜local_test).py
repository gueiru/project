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
def create_knowledge_point(tx, label, relation, obj):
    command = []
    # 查看 node A 是否存在 (類別)
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
    
    # 查看 node B 是否存在
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
    
    
    
    # 查看 node A 與 node B 之間的關係是否存在
    text = "MATCH (a:Categorical {name: '"+label+"'}), (b:"+label+" {name: '"+obj+"'}) RETURN EXISTS((a)-[:"+relation+"]->(b)) AS relationship_exists"
    result = tx.run(text)
    single_result = result.single()
    if single_result is not None:
        exists = single_result["relationship_exists"]
    else:
        exists = False
    
    # 如果關聯不存在，則建立它
    if exists is False:
        text = "MATCH (a:Categorical {name: '"+label+"'}), (b:"+label+" {name: '"+obj+"'}) CREATE (a)-[:"+relation+"]->(b)"
        tx.run(text)
        command.append(text)
        print("Relationship created.")
    else:
        print("Relationship already exists.")
    
    print(command)




#超商
with driver.session() as session:
    convenience_store = ["SevenEleven", "FamilyMart", "萊爾富", "OK", "美廉社"]
    for cv in convenience_store:
        session.write_transaction(create_knowledge_point, "超商", "include", cv)