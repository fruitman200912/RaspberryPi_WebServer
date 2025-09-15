import pymysql

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

session=[]

@app.route("/save/<num>")
def up(num):
    session.append(num)
    print(session)
    return render_template("index.html")

@app.route("/save/<num>")
def up(num):
    '''
        1. numcount 테이블 생성(id, num, insert_at)
        2. pymysql로 연결
        3. 증가 한 수만큼 추가
        4. 연결끊기
        5. db 접속해서 조회
    '''
    return render_template("index.html")
