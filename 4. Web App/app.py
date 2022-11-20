# app.py
from flask import Flask, render_template, request, redirect
from model.exchanges import crawling, graph
from model.database import getLogin
#--------------------------------------------------------------
#Flask 객체 인스턴스 생성
app = Flask(__name__)
#--------------------------------------------------------------
@app.route('/main') # Main
def index():
  return render_template('main.html')
#--------------------------------------------------------------
@app.route('/exchanges', methods=['GET']) # Exchange image
def exchange():
  exc = request.args.get('exc')
  df = crawling(exc)
  graph(df, exc)

  return render_template('exchanges.html', image_file = f"img/graph_{exc}.png")
#--------------------------------------------------------------
@app.route('/') # 로그인
def login():
  return render_template('login.html')
#--------------------------------------------------------------
@app.route('/login_confirm', methods=['POST']) # ID, PW 확인
def login_confirm():
  id = request.form['id']
  pwd = request.form['pwd']

  check = getLogin(id, pwd)
  
  if check == False:
    return redirect('http://127.0.0.1:5000/')
  else:
    return redirect('http://127.0.0.1:5000/main')
#--------------------------------------------------------------
if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
#--------------------------------------------------------------