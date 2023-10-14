from flask import Flask, request, jsonify
import jwt




app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY' #這裡要更改成密碼

@app.route('/login', methods=['POST'])
def login():
    """
    登入
    """

    # 取得使用者輸入的帳號和密碼
    username = request.json['username']
    password = request.json['password']

    # 檢查帳號和密碼是否正確
    if username == 'admin' and password == 'password':
        # 產生使用者 token
        token = jwt.encode({'username': username}, app.config['JWT_SECRET_KEY'], algorithm='HS256')

        return jsonify({'token': token})

    return jsonify({'error': 'Invalid username or password'})

@app.route('/users/me', methods=['POST'])
def get_user_data():
    """
    取得使用者資料
    """
    
    #print(request.headers['Authorization'].split()[1])
    # 取得使用者 JWT 中的 token
    token = request.headers['Authorization'].split()[1]
    print(token)
    # 解析 token
    payload = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    print(payload['username'])
    # 返回使用者資料
    return jsonify({'data': {'username': payload['username']}})
    #return jsonify({'data': {'username': 'yes'}})
if __name__ == '__main__':
    app.run(host='192.168.50.151')