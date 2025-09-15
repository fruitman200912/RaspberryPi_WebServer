import pymysql

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

session=[]

@app.route("/save/<num>")
def up(num):
    session.append(num)
    print(session)
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def save_db():
    data = request.get_json()
    print(data.get("value"))
    conn = pymysql.connetct(host='localhost', user='root', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute(f"insert into numcount(num) values({data.get("value")})")
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
