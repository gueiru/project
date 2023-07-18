import pymysql

connection = pymysql.connect(user="馬賽克", password="馬賽克", host="馬賽克", port=3306, database="credicard", ssl_ca="C:/Users/marslin/Downloads/DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
    
try:
    cursor = connection.cursor()
    query = "SELECT * FROM bank"
    cursor.execute(query)
    for i in cursor:
        print(i)
except Exception as ex:
    print(ex)
cursor.close()
