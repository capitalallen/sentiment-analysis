import tensorflow as tf 
from model_ex import roberta_sentiment_util
import numpy as np 
class ModelExRoberta:
    """
    constructor 
    - load models from h5 files
    - stock-new -sentiment model 
    """
    def __init__(self,folder_path='./config-files/'):
        # load roberta model and tokenizer
        # folder_path, 
        self.tokenizer = roberta_sentiment_util.get_tokenizer(folder_path) 
        self.model = roberta_sentiment_util.load_model(folder_path)
    """
    predict stock buy or sell 
    input: string 
    output: 0 or 1 
    """
    def sentiment_extract(self,text,sentiment):
        # tokenize text 
        input_id_t, attention_mask_t, token_type_id_t, enc = roberta_sentiment_util.tokenize_one(self.tokenizer,text,sentiment)
        # extract text  
        p1,p2 = self.model.predict([input_id_t,attention_mask_t,token_type_id_t],verbose=1)
        p1_max = np.argmax(p1)
        p2_max = np.argmax(p2) 
        return self.tokenizer.decode(enc.ids[p1_max-1:p2_max])
