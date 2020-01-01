import tensorflow as tf 
import matplotlib.pyplot as plt 

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.4):
            print("\nReached 60% accuracy so cancelling training!")
            self.model.stop_training = True
callbacks = myCallback()
# load The Fashion MNIST data 
# available directly in the tf.keras datasets API.
mnist = tf.keras.datasets.fashion_mnist

# load_data: give you two sets of two lists, 
# training and testing values for the graphics that contain the clothing items and their labels.
(training_images,training_labels),(test_images,test_labels) = mnist.load_data()

# print training image and training label 
# plt.imshow(training_images[0])
# print(training_labels[0])
# print(training_images[0])

# for training neural network, it's eaiser to treat all values as between 0 and 1 "normalize"
training_images = training_images/255.0
test_images = test_images/255.0

"""
Design the model 
- Sequential:  defines a sequence of layers in the neural network
- Flatten: just takes that square and turns it into a 1 dimensional set.
- Dense: Adds a layer of neurons
Each layer of neurons need an activation function to tell them what to do. There's lots of options, but just use these for now.
- Relu effectively means "If X>0 return X, else return 0" -- so what it does it it only passes values 0 or greater to the next layer in the network.
- Softmax takes a set of values, and effectively picks the biggest one, so, 
for example, if the output of the last layer looks like 
[0.1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05], 
it saves you from fishing through it looking for the biggest value, 
and turns it into [0,0,0,0,1,0,0,0,0] -- The goal is to save a lot of coding!
"""
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128,activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10,activation=tf.nn.softmax)])

"""
After the model is defined, build the model by compiling it (i.e an optimizer and loss function)
Then, train the model by calling model.fit (asking it to fit your training data to your training labels)
i.e. have it figure out the relationship between the training data and its actual labels
"""
model.compile(optimizer = tf.optimizers.Adam(),loss = 'sparse_categorical_crossentropy',metrics=['accuracy'])
# model.compile(optimizer=tf.train.AdamOptimizer(),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(training_images,training_labels,epochs=5,callbacks=[callbacks])
# print accuracy ratio

# test the model 
model.evaluate(test_images,test_labels)
