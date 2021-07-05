"""
load stock-news-sentiment model 
input: 
    - file_path 
output:
    - model 
"""
import pickle
import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer
def load_model(model_path='./stock-new-sentiment-model.h5'):
    # load model 
    model = tf.keras.models.load_model(model_path) 
    return model

# load tokenizer
def load_tokenizer(tokenizer_path='./tokenizer.pickle'):
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer
load_model()