import tensorflow as tf 
from model_ex import stock_news_sentiment
from keras.preprocessing.sequence import pad_sequences
import numpy as np 
class ModelExGRU:
    """
    constructor 
    - load models from h5 files
    - stock-new -sentiment model 
    """
    def __init__(self):
        # load stock-news model and tokenizer
        self.stock_news_model = stock_news_sentiment.load_model()
        self.stock_news_tokenizer = stock_news_sentiment.load_tokenizer()

    """
    predict stock buy or sell 
    input: string 
    output: 0 or 1 
    """
    def predict_stock_with_news(self,news):
        # tokenize news 
        token = np.array(self.stock_news_tokenizer.texts_to_sequences([news]))
        # predict 
        data_pad = np.array(pad_sequences(token, maxlen = 28))

        pred = float(self.stock_news_model(np.array(data_pad).reshape(1,28))[0][0])
        # # return buy if == 1 elif 0 sell else not recognized
        if pred<0.5:
            return "negative"
        elif pred>0.5:
            return "postive"
        else:
            return "not recognized"
