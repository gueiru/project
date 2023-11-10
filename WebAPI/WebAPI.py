# Flask API
from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import hashlib
from neo4j import GraphDatabase
import networkx as nx


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@localhost:3306/ucard'
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

class banks(db.Model):
  bank_id = db.Column(db.String(3), primary_key=True)
  bank_name = db.Column(db.String(15))

  def __init__(self, bank_id, bank_name):
    self.id = bank_id
    self.name = bank_name

class cards(db.Model):
  bank_id = db.Column(db.String(3), primary_key=True)
  category = db.Column(db.String(1), primary_key=True)
  card_id = db.Column(db.String(3), primary_key=True)
  card_name = db.Column(db.String(20))
  feedback_type = db.Column(db.String(1))
  link = db.Column(db.String(120))

  def __init__(self, bank_id, category, card_id, card_name, feedback_type, link):
    self.bank_id = bank_id
    self.category = category
    self.card_id = card_id
    self.card_name = card_name
    self.feedback_type = feedback_type
    self.link = link

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
  username = email[:email.index("@")]
  return jsonify({'message': 'User logged in successfully','userinf':{'username': username,'email': email,'token': 'token'}}), 200

@app.route('/register', methods=['POST'])
def register():
  email = request.json['email']
  password = request.json['password']
  hashed_password = bcrypt.generate_password_hash(password=password)
  # 檢查是否註冊
  email_check = users.query.filter_by(email=email).first()
  if email_check:
    return jsonify({'message': '電子信箱已註冊過'}), 400
  # Create a new user
  new_user = users(None,email, hashed_password)
  db.session.add(new_user)
  db.session.commit()
  username = email[:email.index("@")]

  return jsonify({'message': 'User registered successfully','userinf':{'username': username,'email': email,'token': 'token'}}), 201

@app.route('/add_bank', methods=['POST'])
def add_bank():
  data = request.json
  for i in range(len(data)):
    print(data[i]['bank_id'] + ' ' + str(data[i]['ischeck']))

  return jsonify({'message': 'Add bank successfully'}),201

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
    content["to"] = email #收件者
    content.attach(MIMEText("臨時密碼："+str(password)+"\n請立即回到app並更改密碼確保資料安全"))  #郵件內容
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:  # 設定SMTP伺服器
      try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.login("ucard112408@gmail.com", "***************")  # 登入寄件者gmail         ######################密碼密碼
        smtp.send_message(content)  # 寄送郵件
        smtp.close()
      except Exception as e:
        print("Error message: ", e)
  
  password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  users.query.filter_by(email=email).update({'password': bcrypt.generate_password_hash(password=password)})
  db.session.commit()
  return jsonify({'message': 'User change password successfully'}), 202

@app.route('/changepwd', methods=['POST'])
def changepwd():
  email = request.json['email']
  password = request.json['password']
  newpassword = request.json['newpassword']
  user = users.query.filter_by(email=email).first()
  #判斷舊密碼是否正確
  if not bcrypt.check_password_hash(user.password, password):
    return jsonify({'message': '密碼錯誤'}), 401
  users.query.filter_by(email=email).update({'password': bcrypt.generate_password_hash(password=newpassword)})
  db.session.commit()
  username = email[:email.index("@")]
  return jsonify({'message': 'User logged in successfully','userinf':{'username': username,'email': email,'token': 'token'}}), 203

@app.route('/getbank', methods=['POST'])
def getbank():
  banklist = banks.query.all()
  # 陣列化資料
  serialized_banks = []
  for bank in banklist:
    serialized_bank = {
      'bank_id': bank.bank_id,
      'bank_name': bank.bank_name
    }
    serialized_banks.append(serialized_bank)
  return jsonify(serialized_banks),203

@app.route('/getcard', methods=['POST'])
def getcard():
  bank_id = request.json['bank_id']
  cardlist = cards.query.filter_by(bank_id=bank_id).all()
  # 陣列化資料
  serialized_cards_visa = []
  serialized_cards_ms = []
  serialized_cards_jcb = []
  for card in cardlist:
    if(card.bank_id == '013' and int(card.card_id) >=101 and int(card.card_id) <=105): #& int(card.card_id) >= 101 & int(card.card_id) <= 105
      if(int(card.card_id) == 101):
        serialized_card = {
          'card_id': card.bank_id + card.category + card.card_id,
          'card_name': '國泰CUBE卡'
        }
      else:
        continue
    else:
      serialized_card = {
        'card_id': card.bank_id + card.category + card.card_id,
        'card_name': card.card_name
      }
    match(card.category):
      case '0':
        serialized_cards_visa.append(serialized_card)
      case '1':
        serialized_cards_ms.append(serialized_card)
      case '2':
        serialized_cards_jcb.append(serialized_card)
  
  return jsonify({'visa':serialized_cards_visa, 'ms':serialized_cards_ms, 'jcb':serialized_cards_jcb}),203

@app.route('/getimg', methods=['GET'])
def getimg():
  imageurl = '/img/' + request.args.get('imageurl')  + '.webp'
  return send_file(imageurl, mimetype='image/webp')

@app.route('/recommend', methods=['GET'])
def recommend():
  uri = "neo4j+s://cd122923.databases.neo4j.io"
  driver = GraphDatabase.driver(uri, auth=("neo4j", "************************")) ######################密碼密碼

  # 定義一個查詢函式
  def run_query(driver, query):
    with driver.session() as session:
      result = session.run(query)
      return result.data()

  # 例子: 執行一個簡單的查詢
  query = "MATCH (n:超商) RETURN n LIMIT 100"

  # 執行查詢
  result = run_query(driver, query)

  result_Array = []
  # 處理結果
  for record in result:
    print(record['n']['name'])
    result_Array.append(record['n']['name'])

  return jsonify({'card':result_Array}),203



if __name__ == '__main__':
  app.run(debug='true',host='192.168.50.151') #192.168.50.151、192.168.176.197
