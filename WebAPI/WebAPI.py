# Flask API
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import hashlib


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@localhost:3306/ucardtest'
db = SQLAlchemy(app)
bcrypt = Bcrypt()

class users(db.Model):
  user_id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150))
  password = db.Column(db.String(60))

  def __init__(self, user_id, email, password):
    self.user_id = user_id
    self.email = email
    self.password = password

@app.route('/login', methods=['POST'])
def login():
  email = request.json['email']
  password = request.json['password']
  # 檢查是使用者是否存在
  user = users.query.filter_by(email=email).first()
  if not user:
    return jsonify({'message': '查無此帳號，請重新輸入'}), 404
  # 確認密碼是否吻合
  if not bcrypt.check_password_hash(user.password, password):
    return jsonify({'message': '密碼錯誤'}), 401
  # 登入成功通知
  return jsonify({'message': 'User logged in successfully','token': email}), 200

@app.route('/register', methods=['POST'])
def register():
  email = request.json['email']
  password = request.json['password']
  hashed_password = bcrypt.generate_password_hash(password=password)
  # 檢查是否註冊
  email_check = users.query.filter_by(email=email).first()
  if email_check:
    return jsonify({'message': '電子信箱已註冊過','token': email}), 400
  # Create a new user
  new_user = users('000001',email, hashed_password)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({'message': 'User registered successfully'}), 201

@app.route('/forgetpw', methods=['POST'])
def forgetpw():
  email = request.json['email']
  user = users.query.filter_by(email=email).first()
  if not user:
    return jsonify({'message': '查無此帳號，請重新輸入'}), 404
  else:
    while True: #執行do-while
      characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" #建立包含數字大小寫英文的字串
      password = "".join([random.choice(characters) for _ in range(8)]) #從上述字串中抽取隨機8碼字元
      uppercase = 0 ; lowercase = 0 ; number = 0 
      for strs in password: #檢查是否有大小寫及數字
        if(strs.isupper()) :
          uppercase += 1
        elif(strs.islower()):
          lowercase += 1
        elif(strs.isdigit()):
          number +=1
      if(lowercase!=0 and number!=0 and uppercase!=0): #檢查是否符合包含大小寫英文及數字如有就不用重新生成
        break  
      
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "Ucard forgot reset"  #郵件標題
    content["from"] = "ucard112408@gmail.com"  #寄件者
    content["to"] = "10946044@ntub.edu.tw" #收件者
    content.attach(MIMEText("臨時密碼："+str(password)+"\n請回到app並更改密碼確保資料安全"))  #郵件內容
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:  # 設定SMTP伺服器
      try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.login("ucard112408@gmail.com", "qcbcezhmnjcupaam")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        smtp.close()
      except Exception as e:
        print("Error message: ", e)

  password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  users.query.filter_by(email=email).update({'password': bcrypt.generate_password_hash(password=password)})
  db.session.commit()
  return jsonify({'message': 'User change password successfully'}), 202

if __name__ == '__main__':
  app.run(debug='true',host='192.168.50.151')
