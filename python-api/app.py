from flask import Flask, request,jsonify
from model_ex import  model_ex_gru, model_ex_roberta
app = Flask(__name__)
# load GRU model class for stock-news prediction 
modelExGRU = model_ex_gru.ModelExGRU()
# load roberta class for sentiment extraction
modelExRoberta = model_ex_roberta.ModelExRoberta()

@app.route("/api/v1/stock-news-sentiment",methods=['POST'])
def predict_stock_news():
    if request.method =='POST':
        try:
            pred = modelExGRU.predict_stock_with_news(request.json['news'])
            return jsonify({'pred':pred}) 
        except:
            return 'service not available', 400

@app.route("/api/v1/sentiment-extraction",methods=['POST'])
def extract_sentiment():
    if request.method=='POST':
        try:
            text, sentiment = request.json['text'],request.json['sentiment']
            pred = modelExRoberta.sentiment_extract(text,sentiment) 
            return jsonify({'pred':pred})
        except:
            return 'service not available', 400
@app.route('/test',methods=['POST','GET'])
def json_example():
    if request.method == 'POST':
        print(request.json['text'])
        return jsonify({'pred':"results"})
    elif request.method == 'GET':
        return jsonify({'pred':"results get"})
    return 'hello'
