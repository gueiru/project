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
  password = db.Column(db.String(256))

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
    return jsonify({'error': 'email already registered'}), 400

  # Create a new user
  #new_user = users(email, password)
  #db.session.add(new_user)
  #db.session.commit()

  return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
  email = request.json['email']
  password = request.json['password']
  email_check = users.query.filter_by(email=email).first()
  #if email_check == "":
  #  print("查無此帳號")
  # return jsonify({'error': 'email not registered'}), 404
  # # Check if email exists
  # user = users.query.filter_by(email=email).first()
  # if not user:
  #   return jsonify({'error': 'email not registered'}), 404
  # # Check if password matches
  # if not check_password_hash(user.password, password):
  #   return jsonify({'error': 'Wrong password'}), 401
  # # Login successful
  # return jsonify({'message': 'User logged in successfully'}), 200
  print(email)
  print(password)
  return jsonify({'message': 'User logged in successfully'}), 200

if __name__ == '__main__':
  app.run(debug=True,host="192.168.50.151")
