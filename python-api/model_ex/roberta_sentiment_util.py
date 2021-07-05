
import tokenizers
import tensorflow as tf 
from transformers import * 
import numpy as np 
"""
get_tokenizer
- input: file_path
- output: tokenizer
"""
def get_tokenizer(folder_path):   
    tokenizer = tokenizers.ByteLevelBPETokenizer(
        vocab_file=folder_path+'vocab-roberta-base.json', 
        merges_file=folder_path+'merges-roberta-base.txt', 
        lowercase=True,
        add_prefix_space=True
    )
    return tokenizer 
"""
return input_ids, attention_mask, type_ids and enc for roberta model predict
"""
def tokenize_one(tokenizer,text,sentiment):
    MAX_LEN=96
    ct = 1
    sentiment_id = {'positive': 1313, 'negative': 2430, 'neutral': 7974}
    input_ids_t = np.ones((ct,MAX_LEN),dtype='int32')
    attention_mask_t = np.zeros((ct,MAX_LEN),dtype='int32')
    token_type_ids_t = np.zeros((ct,MAX_LEN),dtype='int32')
    text1 = " "+" ".join(text.split())
    enc = tokenizer.encode(text1)                
    s_tok = sentiment_id[sentiment]
    input_ids_t[0,:len(enc.ids)+5] = [0] + enc.ids + [2,2] + [s_tok] + [2]
    attention_mask_t[0,:len(enc.ids)+5] = 1
    return input_ids_t,attention_mask_t, token_type_ids_t,enc

"""
build roberta model 
- output: model 
"""
def build_model(folder_path):
    MAX_LEN = 96
    ids = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
    att = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
    tok = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)

    config = RobertaConfig.from_pretrained(folder_path+'config-roberta-base.json')
    bert_model = TFRobertaModel.from_pretrained(folder_path+'pretrained-roberta-base.h5',config=config)
    x = bert_model(ids,attention_mask=att,token_type_ids=tok)
    
    x1 = tf.keras.layers.Dropout(0.1)(x[0]) 
    x1 = tf.keras.layers.Conv1D(1,1)(x1)
    x1 = tf.keras.layers.Flatten()(x1)
    x1 = tf.keras.layers.Activation('softmax')(x1)
    
    x2 = tf.keras.layers.Dropout(0.1)(x[0]) 
    x2 = tf.keras.layers.Conv1D(1,1)(x2)
    x2 = tf.keras.layers.Flatten()(x2)
    x2 = tf.keras.layers.Activation('softmax')(x2)

    model = tf.keras.models.Model(inputs=[ids, att, tok], outputs=[x1,x2])
    optimizer = tf.keras.optimizers.Adam(learning_rate=3e-5)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model 

"""
build model and load model weight
return model with weights 

"""
def load_model(folder_path):
    model = build_model(folder_path) 
    model.load_weights(folder_path+"trained_model_weight.h5")
    return model