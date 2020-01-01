import tensorflow as tf
import numpy as np
from tensorflow import keras
def gethousePrice(n):
    ans=[]
    for i in range(1,n+1):
        ans.append(50+i*50)
    print(ans)
gethousePrice(7)

# GRADED FUNCTION: house_model
def house_model(y_new):
    xs = np.array([0,1,2,3,4,5,6],dtype=int)# Your Code Here#
    ys = np.array([50,100,150,200,250,300,350],dtype=int)# Your Code Here#
    
    model = keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])# Your Code Here#
    model.compile(optimizer='sgd',loss='mean_squared_error')
    model.fit(xs,ys,epochs=2000)
    return model.predict(y_new)[0]

prediction = house_model([7.0])
print(prediction)

