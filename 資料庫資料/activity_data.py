import pymysql
import math
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='ucardtest',
                            #ssl_ca='C:\Program Files (x86)\OpenSSL-Win32\DigiCertGlobalRootCA.crt.pem', ssl_disabled=False
                            )
import pandas as pd
df = pd.read_excel("短期資料整理.xlsx",sheet_name="短期")
#print(df)
print(len(df))#總比數
for i in range(len(df)):
    if df["銀行別"][i]== 13:
            bank=("0"+str(df["銀行別"][i]))

            category=str(df["發卡商"][i])

            if len(str(df["號碼"][i]))==1:
                id="00"+ str(df["號碼"][i])
            elif len(str(df["號碼"][i]))==2:
                id="0"+ str(df["號碼"][i])
            else :  
                id=str(df["號碼"][i])
            
            back=float(df["回饋"][i])

            title=str(df["標題"][i])

            start=str(df["開始"][i])

            
            end=str(df["結束"][i])

            store=str(df["店家"][i])
            if store=="nan":
                 store=None

            note=str(df["備註"][i])
            if note=="nan":
                 note=None

            address=str(df["網址"][i])

            state=str(df["狀態"][i])

            #print("輸出",id,category,back,bank,title,start,end,condition,limit,store,note,address,state)
    #print("cond型態",type(condition))
    #print("cond值",type(condition))
    #print("lim",type(limit))
    #print("lim輸出",limit)

            try:
                cursor = connection.cursor()
                query = "INSERT INTO activity (bank,category,id,title,start,end,`back`,store,note,address,state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (bank,category,id,title,start,end,back,store,note,address,state))
                connection.commit()
                for i in cursor:
                    print(i)
            except pymysql.connect.Error as e:
                    print("Error: Could not make connecion to the MySQL database")
                    print(e)




'''
for i in range(len(df)):
    if len(str(df["銀行"][i]))==2:
        bank=("0"+str(df["銀行"][i]))
    else:
        bank=str(df["銀行"][i])
    
    category=str(df["發行商"][i])
    
    if len(str(df["號碼"][i]))==1:
        id="00"+ str(df["號碼"][i])
    elif len(str(df["號碼"][i]))==2:
          id="0"+ str(df["號碼"][i])
    else :  
        id=str(df["號碼"][i])

    name=str(df["名稱"][i])
    address=str(df["網址"][i])
    
'''

        
    #print (bank,c,id,name,address)
