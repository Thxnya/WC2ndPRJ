# app.py
from flask import Flask, render_template, request

#--------------------------------------------------------------
#Flask 객체 인스턴스 생성
app = Flask(__name__)
#--------------------------------------------------------------
@app.route('/') # 접속하는 url
def index():
  return render_template('demo1.html')
#--------------------------------------------------------------
# 시간
@app.route('/time') # 접속하는 url
def time():
  val = request.args.get('val')
  return render_template('time.html', val=val)
#--------------------------------------------------------------
# 테스트
@app.route('/test') # 접속하는 url
def test():
  return render_template('demo1.html')
#--------------------------------------------------------------
if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
#--------------------------------------------------------------