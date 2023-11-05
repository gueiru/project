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
def create_knowledge_point(tx, label, relation, obj):
    command = []
    
    # 查看 node A 是否存在 (類別)
    text = "MATCH (n:Categorical {name: $label}) RETURN n"
    result = tx.run(text, label=label)    
    # 檢查查詢結果
    if not result.peek():
        # 如果節點不存在，則建立它
        text = "CREATE (" + label + ":Categorical {name: $label})"
        tx.run(text, label=label)
        command.append(text)
        print("Node created.")
    else:
        print("Node already exists.")
    print(command)
    
    # 查看 node B 是否存在
    text = "MATCH (n:"+label+" {name: $obj}) RETURN n"
    result = tx.run(text, obj=obj)
    # 檢查查詢結果
    if not result.peek():
        # 如果節點不存在，則建立它
        text = "CREATE (" + obj + ":" + label + " {name: $obj})"
        tx.run(text, obj=obj)
        command.append(text)
        print("Node created.")
    else:
        print("Node already exists.")
    print(command)


    # 查看 node A 與 node B 之間的關係是否存在
    text = "MATCH (a:Categorical {name: $label}), (b:" + label + " {name: $obj}) RETURN EXISTS((a)-[:" + relation + "]->(b)) AS relationship_exists"
    result = tx.run(text, label=label, obj=obj)
    single_result = result.single()
    if single_result is not None:
        exists = single_result["relationship_exists"]
    else:
        exists = False
    
    # 如果關聯不存在，則建立它
    if exists is False:
        text = "MATCH (a:Categorical {name: $label}), (b:" + label + " {name: $obj}) CREATE (a)-[:" + relation + "]->(b)"
        tx.run(text, label=label, obj=obj)
        command.append(text)
        print("Relationship created.")
    else:
        print("Relationship already exists.")
    
    print(command)

#-------------------------------以下為建立資料庫的code------------------------------------------

# 國內餐飲
with driver.session() as session:
    restaurants = [
        "王品牛排", "TASTy西堤牛排", "丰龢和牛涮", "肉次方燒肉放題", "Oh_my原燒",
        "和牛涮", "尬鍋台式潮鍋", "聚北海道昆布鍋", "石二鍋", "青花驕",
        "_12MINI", "陶板屋", "藝奇和牛岩板焼", "夏慕尼新香榭鐵板燒", "品田牧場",
        "享鴨", "hot7鐵板燒", "莆田", "築間幸福鍋物", "燒肉Smile",
        "有之和牛鍋物放題", "本格和牛燒肉放題", "繪馬別邸", "瓦城泰國料理", 
        "非常泰概念餐坊", "_1010湘", "大心新泰式麵食", "時時香RICE_BAR", "YABI_KITCHEN", 
        "月月THAI_BBQ", "樂子The_Dinner", "茹絲葵經典牛排館", "屋馬燒肉", "solo_pasta義大利麵", 
        "俺達の肉屋_日本和牛專門店", "鹽之華法式餐廳", "廚房有雞花雕雞", "碳佐麻里精品燒肉", 
        "与玥樓頂級粵菜餐廳", "RAW", "山海樓", "金蓬萊遵古台菜餐廳", "老新台菜", 
        "麥當勞", "星巴克",
        "台北萬豪酒店", "君悅酒店", "台北遠東香格里拉", "台南遠東香格里拉", "中山招待所",
        "高雄萬豪酒店", "台北寒舍艾美酒店", "台北美福大飯店", "台北晶華酒店", "文華東方酒店",
        "維多麗亞酒店", "漢來名人坊", "瑞穗天合國際觀光酒店", "JR東日本大飯店", "台北美食地標Mega50",
        "新北美食地標Mega50", "新竹國賓大飯店", "林酒店", "高雄林皇宮", "台中長榮桂冠酒店",
        "大地酒店", "台北國泰萬怡酒店", "台北六福萬怡酒店"
    ]
    for r in restaurants:
        session.write_transaction(create_knowledge_point, "國內餐飲", "include", r)
print("----------------------------------------------------------------")

# 台塑關係企業
with driver.session() as session:
    relation = [
        "台塑生醫", "長庚生技", "台塑購物網", "台塑網旅行社"
    ]
    for r in relation:
        session.write_transaction(create_knowledge_point, "台塑關係企業", "include", r)

# 娛樂
with driver.session() as session:
    ent = [
        "錢櫃KTV", "好樂迪KTV", "星聚點KTV", "享溫馨KTV", 
        
        "國賓影城", "威秀影城", "ShowTimes秀泰影城"
    ]
    for e in ent:
        session.write_transaction(create_knowledge_point,"娛樂", "include", e)
print("----------------------------------------------------------------")

# 停車場
with driver.session() as session:
    park = [
        "城市車旅", "嘟嘟房"
    ]
    for p in park:
        session.write_transaction(create_knowledge_point,"停車場", "include", p)
print("----------------------------------------------------------------")

# 超市
with driver.session() as session:
    markets = [
        "家樂福", "全聯福利中心"
    ]
    for m in markets:
        session.write_transaction(create_knowledge_point,"超市", "include", m)
print("----------------------------------------------------------------")

#飯店住宿
with driver.session() as session:
    hotels = [
        "台北遠東香格里拉", "台南遠東香格里拉", "新竹國賓大飯店", "馥蘭朵烏來渡假酒店", "馥蘭朵墾丁渡假酒店",
        "馥森里山藝術生態園", "馥森阪治Trio", "花蓮理想大地"
    ]
    for h in hotels:
        session.write_transaction(create_knowledge_point, "飯店住宿", "include", h)
print("----------------------------------------------------------------")

# 旅行社
with driver.session() as session:
    travel_agencies = [
        "ezTravel易遊網", "雄獅旅遊","可樂旅遊", "東南旅遊", "五福旅遊",
        "燦星旅遊", "山富旅遊", "長汎假期","鳳凰旅行社", "Ezfly易飛網",
        "理想旅遊", "永利旅行社", "三賀旅行社", "台塑網旅行社" 
    ]
    for ta in travel_agencies:
        session.write_transaction(create_knowledge_point, "旅行社", "include", ta)
print("----------------------------------------------------------------")

# 訂房平台
with driver.session() as session:
	travel_platforms = [
        "KKday", "Agoda", "KLOOK", "Airbnb", "Hotels_com",
        "Expedia", "Booking_com", "Trip_com", "AsiaYo"
		]
	for plt in travel_platforms:
	        session.write_transaction(create_knowledge_point, "訂房平台", "include", plt)
print("----------------------------------------------------------------")

# 百貨公司
with driver.session() as session:
    shopping_centers = [
        "遠東SOGO百貨", "太平洋百貨", "新光三越", "SKM_Park", "遠東百貨",
        "Big_City遠東巨城購物中心", "微風廣場", "誠品生活", "環球購物中心", "CITYLINK",
        "BELLAVITA", "統一時代", "台北101", "ATT_4_FUN", "明曜百貨", "京站",
        "美麗華", "大葉高島屋", "遠企購物中心", "比漾廣場", "大江國際購物中心",
        "中友百貨", "廣三SOGO", "Tiger_City", "勤美誠品綠園道", "金典綠園道",
        "大魯閣新時代", "耐斯廣場", "南紡購物中心", "德安百貨", "夢時代", "大立百貨",
        "大統百貨", "漢神百貨", "漢神巨蛋",
        "林口MITSUI_OUTLET_PARK", "台中港MITSUI_OUTLET_PARK", "台南MITSUI_OUTLET_PARK",
        "台中Mitsui_Shopping_Park_LaLaport", "禮客", "義大世界購物廣場", "華泰名品城",
        "義享天地", "麗寶OUTLET_Mall", "麗寶百貨廣場", "秀泰生活", "徐匯廣場",
        "台茂購物中心", "桃園統領百貨", "新月廣場", "日曜天地", "三創生活", "_6_Plaza廣場",
        "iFG遠雄廣場", "台南FOCUS", "悅誠廣場", "欣欣百貨", "宏匯廣場",
        "高雄棧貳庫商場", "樂購廣場", "NOKE忠泰樂生活", "昇恆昌"
    ]
    for shop in shopping_centers:
        session.write_transaction(create_knowledge_point, "百貨公司", "include", shop)
print("----------------------------------------------------------------")
       
# 國內藥妝
with driver.session() as session:
    pharmacies = [
        "康是美", "寶雅", "屈臣氏", "日藥本舖", "Tomod_s", "松本清"
    ]
    for p in pharmacies:
        session.write_transaction(create_knowledge_point, "國內餐飲", "include", p)
print("----------------------------------------------------------------")

# 外送平台
with driver.session() as session:
    food_delivery_platforms = [
        "Uber_Eats", "foodpanda", "foodomo", "inline"
    ]
    for p in food_delivery_platforms:
        session.write_transaction(create_knowledge_point, "外送平台", "include", p)
print("----------------------------------------------------------------")

#超商
with driver.session() as session:
    convenience_store = ["SevenEleven", "FamilyMart", "萊爾富", "OK", "美廉社"]
    for cv in convenience_store:
        session.write_transaction(create_knowledge_point, "超商", "include", cv)
print("----------------------------------------------------------------")

# 影音串流平台
with driver.session() as session:
    musics = [
        "Google_Play", "Disney_Plus", "Netflix", "Spotify", "KKBOX", "KKTV",
        "App_Store", "Apple_Music", "iCloud"
    ]
    for music in musics:
        session.write_transaction(create_knowledge_point, "串流平台", "include", music)
print("----------------------------------------------------------------")

#電商平台
with driver.session() as session:
    shopping_websites = [
        "蝦皮購物", "momo購物網", "PChome線上購物", "Yahoo奇摩購物中心", "小樹購",
        "蝦皮商城", "Amazon", "淘寶", "天貓", "博客來"
    ]
    for shop in shopping_websites:
        session.write_transaction(create_knowledge_point, "電商", "include", shop)
print("----------------------------------------------------------------")

#支付方式
with driver.session() as session:
    PayList = [
        "歐付寶", "橘子支付", "ezPay簡單付", "街口支付", "全盈_PAY", "全支付" 
        "PChome國際連", "一卡通Money", "悠遊付", "icash_Pay", "LinePay", 
        "Apple_Pay", "Samsung_Pay", "Google_Pay", "台灣Pay", "玉山Wallet", 
        "Hami_Pay", "OPEN錢包"
    ]
    for pay in PayList:
        session.write_transaction(create_knowledge_point, "支付方式", "include", pay)
print("----------------------------------------------------------------")
      
#交通
with driver.session() as session:
    Traffic_List = ["高鐵", "計程車", "公車", "台鐵", "捷運", "飛機"
					"Uber", "LINE_TAXI", "yoxi", "台灣大車隊", "大都會計程車",
					"和運租車", "iRent", "格上租車", "中租租車", "AVIS租車",
                    "台灣中油_直營店"
     ]
    for transportation in Traffic_List:
        session.write_transaction(create_knowledge_point, "交通", "include", transportation)
print("----------------------------------------------------------------")

print("------------------done------------------")