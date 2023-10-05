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


#新增專區，要備份到"全部備份"的檔案