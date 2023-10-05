# Flask API
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/ucardtest'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))

  def __init__(self, username, password):
    self.username = username
    self.password = password

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def home():
  return "<h1>hello</h1>"

@app.route('/register', methods=['POST'])
def register():
  username = request.json['username']
  password = request.json['password']
  # Check if email already exists
  user = users.query.filter_by(username=username).first()
  if user:
    return jsonify({'error': 'Email already registered'}), 400
  # Hash the password
  hashed_password = generate_password_hash(password)
  # Create a new user
  new_user = users(username, hashed_password)
  db.session.add(new_user)
  db.session.commit()
  return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
  username = request.json['username']
  password = request.json['password']
  # Check if email exists
  user = users.query.filter_by(username=username).first()
  if not user:
    return jsonify({'error': 'username not registered'}), 404
  # Check if password matches
  if not check_password_hash(user.password, password):
    return jsonify({'error': 'Wrong password'}), 401
  # Login successful
  return jsonify({'message': 'User logged in successfully'}), 200

if __name__ == '__main__':
  app.run(debug=True,host="192.168.50.151")
