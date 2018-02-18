from flask import Flask

app = Flask(__name__)

@app.route('/login/<userid>')
def hello_world(userid):
    return 'id는 ' + userid + '입니다.  '

#서버 구동

@app.route('/hello')
def hello():
    return 'hello'



app.run(host='127.0.0.1')