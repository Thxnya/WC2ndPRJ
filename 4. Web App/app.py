# app.py
from flask import Flask, render_template, request
from model.exchanges import crawling, graph
#--------------------------------------------------------------
#Flask 객체 인스턴스 생성
app = Flask(__name__)
#--------------------------------------------------------------
@app.route('/') # Main
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
@app.route('/test') # test
def test():
  return render_template('exchanges copy.html')
#--------------------------------------------------------------
if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
#--------------------------------------------------------------