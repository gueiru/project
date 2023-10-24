from neo4j import GraphDatabase
import networkx as nx
import matplotlib.pyplot as plt

#更改Neo4j Bolt連線設定
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Test20020422"))

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


#-------------------------------以下為建立資料庫的code------------------------------------------
# 國泰卡片
with driver.session() as session:
    card8 = ["蝦皮購物聯名卡", "長榮航空聯名卡", "CUBE卡", "國泰世界卡",
            "亞洲萬里通聯名卡", "台塑聯名卡", "雙幣卡", "eTag聯名卡"]
    for card in card8:
        session.write_transaction(create_knowledge_point, "國泰信用卡", "include", card)

# 富邦卡片
with driver.session() as session:
    card20 = [ "富邦J卡", "富邦IMPERIAL尊御世界卡", "富邦數位生活卡",
            "富邦鑽保卡", "富邦財神系列卡", "Open_Possible聯名卡",
            "富邦世界卡", "富邦無限卡", "富邦富利生活系列卡", "富邦鈦金卡",
            "富邦銀行卡", "富邦Costco聯名卡", "momo卡", "富邦悍將悠遊聯名卡",
            "台茂聯名卡", "廣三SOGO聯名卡", "采盟聯名卡",
            "DHC聯名卡", "福華聯名卡", "麗嬰房聯名卡"]
    for card in card20:
        session.write_transaction(create_knowledge_point, "富邦信用卡", "include", card)

# 中信卡片
with driver.session() as session:
    card49 = ["Agoda聯名卡", "Mitsui_Shopping_Park_LaLaport聯名卡", "ALL_ME卡",
             "LINE_Pay信用卡", "英雄聯盟信用卡", "中油聯名卡",
             "中信商旅鈦金卡", "TAIPEI_101聯名卡(尊榮鼎極卡)", "TAIPEI_101聯名卡(新鼎極卡)",
            "TAIPEI_101聯名卡(新御璽卡)", "和泰聯名卡","中國信託鼎極卡(無限卡/極緻卡)",
            "中國信託鼎極卡(世界卡)", "中信紅利御璽卡","中信紅利晶緻卡",
            "中信現金回饋御璽卡","中信現金回饋鈦金卡","中信紅利卡",
            "寰遊美國運通卡","Super_Life_VISA卡", "中信兄弟聯名卡(鼎極卡)",
            "中信兄弟聯名卡(御璽/鈦金卡)","中信兄弟聯名卡(白金卡)","中信兄弟聯名卡(不限卡別)",
            "LEXUS聯名卡","中信商務卡/雙幣商務卡","中華電信聯名卡",
            "漢神百貨聯名卡(無限卡)","漢神百貨聯名卡(世界卡)", "漢神百貨聯名卡(御璽卡)",
            "漢神百貨聯名卡(晶緻卡)", "漢神百貨聯名卡(鈦金卡)","Global_Mall聯名卡(無限卡)",
            "Global_Mall聯名卡(御璽卡)","Global_Mall聯名卡(白金卡)","秀泰聯名卡(晶緻卡)",
            "秀泰聯名卡(白金卡)","大葉髙島屋百貨聯名卡(世界卡)", "大葉髙島屋百貨聯名卡(無限卡)",
            "大葉髙島屋百貨聯名卡(鈦金卡)","大葉髙島屋百貨聯名卡(御璽卡/晶緻卡)","大葉髙島屋百貨聯名卡(白金卡)",
            "南紡購物中心聯名卡(鼎極無限卡)","南紡購物中心聯名卡(御璽卡)","勤美天地聯名卡(御璽卡/晶緻卡)",   
            "勤美天地聯名卡(白金卡)","MUJI無印良品聯名卡", "酷玩卡",
            "統一企業認同卡"]
    for card in card49:
        session.write_transaction(create_knowledge_point, "中信信用卡", "include", card)

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



print("done")