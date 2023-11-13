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
    # 檢查 from_node 是否存在
    check_from_node_query = "MATCH (from_node {name: $from_node_name}) RETURN from_node"
    from_node_exists = tx.run(check_from_node_query, from_node_name=from_node_name)

    if not from_node_exists.single():
        print(f"！！！！！！Node '{from_node_name}' does not exist！！！！！！")
        return

    for to_node_name in to_node_names:
        # 檢查 to_node 是否存在
        check_to_node_query = "MATCH (to_node {name: $to_node_name}) RETURN to_node"
        to_node_exists = tx.run(check_to_node_query, to_node_name=to_node_name)

        if not to_node_exists.single():
            print(f"！！！！！Node '{to_node_name}' does not exist！！！！！")
        else:
            # 如果節點存在，則建立關聯
            merge_query = (
                "MATCH (from_node {name: $from_node_name}) "
                "MATCH (to_node {name: $to_node_name}) "
                "MERGE (from_node)-[r:" + relation_type + "]->(to_node) "
                "RETURN r"
            )

            result = tx.run(merge_query, from_node_name=from_node_name, to_node_name=to_node_name)

            if result.peek():
                print("--Relationship existed--")
            else:
                print("++Relationship created++")


#-------------------------------以下為建立資料庫的 code------------------------------------------
# ALL_ME卡
with driver.session() as session:
    rewards = [
        "SevenEleven711", "全家FamilyMart", "萊爾富", "OK", "美廉社",
        "小北百貨", "棉花田生機園地", 
        "台鐵", "台灣大車隊", "嘟嘟房", "路邊停車",
        "屈臣氏", "cosmed康是美", "poya寶雅", "松本清", "日藥本舖",
        "三井3c", "順發3c", "京站時尚廣場", "美麗華百樂園",
        "宏匯廣場", "三創生活園區", "屏東太平洋百貨",
        
    ]
    session.write_transaction(create_relationship, "ALL_ME卡", rewards, "reward")

# Mitsui_Shopping_Park_LaLaport聯名卡
with driver.session() as session:
    rewards = [
        "台中Mitsui_Shopping_Park_LaLaport"
    ]
    session.write_transaction(create_relationship, "Agoda聯名卡", rewards, "reward")

# Agoda聯名卡
with driver.session() as session:
    rewards = [
        "Agoda"
    ]
    session.write_transaction(create_relationship, "Agoda聯名卡", rewards, "reward")

print("-------------done----------")
