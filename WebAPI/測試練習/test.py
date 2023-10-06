# Flask API
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@localhost:3306/ucardtest'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class users(db.Model):
  userid = db.Column(db.String(256), primary_key=True)
  password = db.Column(db.String(256))

  def __init__(self, userid, password):
    self.userid = userid
    self.password = password

class UserSchema(ma.Schema):
  class Meta:
    fields = ('userid', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def home():
  return "<h1>hello</h1>"

@app.route('/register', methods=['POST'])
def register():
  userid = request.json['userid']
  password = request.json['password']
  # 檢查是否註冊
  userid_check = users.query.filter_by(userid=userid).first()
  if userid_check:
    return jsonify({'error': 'userid already registered'}), 400

  # Create a new user
  #new_user = users(userid, password)
  #db.session.add(new_user)
  #db.session.commit()
  return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
  userid = request.json['userid']
  password = request.json['password']
  userid_check = users.query.filter_by(userid=userid).first()
  #if userid_check == "":
  #  print("查無此帳號")
  # return jsonify({'error': 'userid not registered'}), 404
  # # Check if email exists
  # user = users.query.filter_by(userid=userid).first()
  # if not user:
  #   return jsonify({'error': 'userid not registered'}), 404
  # # Check if password matches
  # if not check_password_hash(user.password, password):
  #   return jsonify({'error': 'Wrong password'}), 401
  # # Login successful
  # return jsonify({'message': 'User logged in successfully'}), 200
  print(userid)
  print(password)
  return jsonify({'message': 'User logged in successfully'}), 200

if __name__ == '__main__':
  app.run(debug=True,host="192.168.50.151")
