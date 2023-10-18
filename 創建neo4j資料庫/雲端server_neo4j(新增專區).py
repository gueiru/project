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
def create_knowledge_point(tx, label, relation, obj):
    command = []
    # 查看 node A 是否存在 (類別)
    text = "MATCH (n:Categorical {name: $label}) RETURN n"
    result = tx.run(text, label=label)
    # 檢查查詢結果
    if not result.peek():
        # 如果節點不存在，則建立它
        text = "CREATE (:" + label + ":Categorical {name: $label})"
        tx.run(text, label=label)
        command.append(text)
        print("Node created.")
    else:
        print("Node already exists.")
    print(command)
    
    # 查看 node B 是否存在
    text = "MATCH (n:" + label + " {name: $obj}) RETURN n"
    result = tx.run(text, obj=obj)
    # 檢查查詢結果
    if not result.peek():
        # 如果節點不存在，則建立它
        text = "CREATE (:" + label + " {name: $obj})"
        tx.run(text, obj=obj)
        command.append(text)
        print("Node created.")
    else:
        print("Node already exists.")
    print(command)
    
    # 查看 node A 與 node B 之間的關係是否存在
    text = "MATCH (a:Categorical {name: $label}), (b:" + label + " {name: $obj}) RETURN EXISTS((a)-[:" + relation + "]->(b)) AS relationship_exists"
    result = tx.run(text, label=label, obj=obj, relation=relation)
    single_result = result.single()
    exists = single_result["relationship_exists"] if single_result else False
    
    # 如果關聯不存在，則建立它
    if not exists:
        text = "MATCH (a:Categorical {name: $label}), (b:" + label + " {name: $obj}) CREATE (a)-[:" + relation + "]->(b)"
        tx.run(text, label=label, obj=obj, relation=relation)
        command.append(text)
        print("Relationship created.")
    else:
        print("Relationship already exists.")
    
    print(command)


#-------------------------------以下為建立資料庫的code------------------------------------------



#超商
with driver.session() as session:
    convenience_store = ["SevenEleven", "FamilyMart", "萊爾富", "OK", "美廉社"]
    for cv in convenience_store:
        session.write_transaction(create_knowledge_point, "超商", "include", cv)

# 影音串流平台
with driver.session() as session:
    musics = ["Google_Play", "Disney_Plus", "Netflix", "Spotify", "KKBOX", "KKTV"]
    for music in musics:
        session.write_transaction(create_knowledge_point, "串流平台", "include", music)

#電商平台
with driver.session() as session:
    shopping_websites = ["蝦皮購物", "momo購物網", "PChome線上購物", "Yahoo奇摩購物中心", "小樹購"]
    for shop in shopping_websites:
        session.write_transaction(create_knowledge_point, "電商", "include", shop)

#支付方式
with driver.session() as session:
    PayList = ["歐付寶", "橘子支付", "ezPay簡單付", "街口支付", "全盈_PAY", "全支付" 
                         "PChome國際連", "一卡通Money", "悠遊付", "icash_Pay", "LINE_Pay", 
                         "Apple_Pay", "Samsung_Pay", "Google_Pay", "台灣Pay", "玉山Wallet", 
                         "Hami_Pay"]
    for pay in PayList:
        session.write_transaction(create_knowledge_point, "支付方式", "include", pay)
        
#交通
with driver.session() as session:
    Traffic_List = ["高鐵", "計程車", "公車", "台鐵", "捷運", "飛機"]
    for transportation in Traffic_List:
        session.write_transaction(create_knowledge_point, "交通", "include", transportation)



print("--------------------done------------------")