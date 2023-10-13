# Flask API
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@localhost:3306/ucardtest'
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt()

class users(db.Model):
  email = db.Column(db.String(150), primary_key=True)
  password = db.Column(db.String(60))

  def __init__(self, email, password):
    self.email = email
    self.password = password

class UserSchema(ma.Schema):
  class Meta:
    fields = ('email', 'password')

users_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def home():
  return "<h1>hello</h1>"

@app.route('/register', methods=['POST'])
def register():
  email = request.json['email']
  password = request.json['password']
  bcrypt.generate_password_hash(password=password)
  hashed_password = bcrypt.generate_password_hash(password=password)
  # 檢查是否註冊
  email_check = users.query.filter_by(email=email).first()
  if email_check:
    return jsonify({'message': '電子信箱已註冊過'}), 400
  has_password = hashed_password[2:-1] #可以刪除前面的b'以及後面的'
  # Create a new user
  new_user = users(email, hashed_password)
  print(email)
  print(hashed_password)
  print(has_password)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
  email = request.json['email']
  password = request.json['password']
  print(email)
  print(password)
  # 檢查是使用者是否存在
  user = users.query.filter_by(email=email).first()
  if not user:
    return jsonify({'message': '查無此帳號，請重新輸入'}), 404
  # Check if password matches
  if not bcrypt.check_password_hash(user.password, password):
    return jsonify({'message': '密碼錯誤'}), 401
  # Login successful
  return jsonify({'message': 'User logged in successfully'}), 200

if __name__ == '__main__':
  app.run(debug=True,host="192.168.50.151")
