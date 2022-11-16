# app.py
from flask import Flask, render_template, request
from model.exchanges import crawling, graph

#--------------------------------------------------------------
#Flask 객체 인스턴스 생성
app = Flask(__name__)
#--------------------------------------------------------------
@app.route('/') # 접속하는 url
def index():
  df = crawling()
  graph(df)

  return render_template('test.html')
#--------------------------------------------------------------
# 시간
@app.route('/time') # 접속하는 url
def time():
  val = request.args.get('val')
  return render_template('time.html', val=val)
#--------------------------------------------------------------
# 테스트
@app.route('/ajax') # 접속하는 url
def test():
  return render_template('demo1.html')
#--------------------------------------------------------------
# 환율정보
@app.route('/main') # 접속하는 url
def main():
  return render_template('main.html')
#--------------------------------------------------------------
# Processing
@app.route('/proc') # 접속하는 url
def proc():
  return render_template('proc.html')
#--------------------------------------------------------------
if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
#--------------------------------------------------------------