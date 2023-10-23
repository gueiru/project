
import pymysql
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='ucardtest',
                            #ssl_ca='C:\Program Files (x86)\OpenSSL-Win32\DigiCertGlobalRootCA.crt.pem', ssl_disabled=False
                            )
import pdfplumber
pdf = pdfplumber.open('D:\大學專題/202308+小額特店資料.pdf')   # 開啟 pdf
page_count = len(pdf.pages) #總頁數
a=0
for t in range(page_count):
    page = pdf.pages[t]           # 讀取頁數
    table = page.extract_table()  # 取出表格
    c=len(table)#單頁總項目
    for b in range(c):
        name=table[b][1]
        try:
            cursor = connection.cursor()
            query = "INSERT INTO ncc (name) VALUES (%s)"
            cursor.execute(query, (name))
            connection.commit()
            for i in cursor:
                print(i)
        except pymysql.connect.Error as e:
                print("Error: Could not make connecion to the MySQL database")
                print(e)
        
                    
#print(table[1][1]) #取出第二項


""" connection = pymysql.connect(host='projecttest.mysql.database.azure.com',
                             user='10946032',
                             password='Ab10946032@',
                             db='credicard',
                            ssl_ca='C:\Program Files (x86)\OpenSSL-Win32\DigiCertGlobalRootCA.crt.pem', ssl_disabled=False) """




cursor.close()
connection.close()
pdf.close()
