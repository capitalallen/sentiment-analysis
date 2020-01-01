"""
use features to distinguish one item from another 
add some layers to do convolution before dense layers 
take longer but higher accuracy 
"""
import tensorflow as tf 
mnist = tf.keras.datasets.fashion_mnist 
(training_images,training_labels),(test_images,test_labels) = mnist.load_data() 
# reshape the data from 60000 28*28*1 items in a list to D list that is 60000*28*28*1
training_images=training_images.reshape(60000, 28, 28, 1)
training_images=training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images=test_images/255.0

model = tf.keras.models.Sequential([
    #convolution layer and pooling layer 
    #param: size of the convolution (3*3 grid); the activation  function to sue (relu)
    #       the shape of the input data  
    tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)),
    # pooling  layer: quarter the szie of the iamge 
    tf.keras.layers.MaxPooling2D(2,2),
    # another convolution
    tf.keras.layers.Conv2D(64,(2,2),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # flatthen the output 
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()
model.fit(training_images,training_labels,epochs=5)
test_loss=model.evaluate(test_images,test_labels)
print(test_loss)

 