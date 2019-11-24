"""
Author: Daniel Herrera
Date: Nov 23, 2019
DESC: custom tensorflow deep learning neural network.
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.system('cls') # clears all the tensorflow deprication warnings.
'''
FEEDFORWARD NEURAL NETWORK
input > weight > hidden L1 (activation function) > weights > hidden L2 (activation func)
> weights > output layer

Backpropogation:
compare(output to intended output) - using cost|loss function (cross entropy)
optimizer function > minimize cost (AdamOptimizer,...SGD, AdaGrad, etc)

FF + BACKPROP = epoch

'''
# defining topoligical standings
n_node_hl1 = 500
n_node_hl2 = 500
n_node_hl3 = 500

n_classes = 10
batch_size = 100 # the amount of batch data sets being loaded into memory at a time
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

#10 class [0,9]
''' one_hot -> represent an element that is going to be turned on
    <0,1,2,3,4,5,6,7,8,9>
0 = [1,0,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0,0]
'''

# matrix = height x width
x = tf.placeholder('float', [None, 784]) # data
y = tf.placeholder('float') # label


#method defining the shape of the layers
def neural_network_model(data):
    # input_data * weights + bias
    hidden_1_layer = {'weights' : tf.Variable(tf.random_normal([784, n_node_hl1])),
                      'biases' : tf.Variable(tf.random_normal([n_node_hl1]))} # specifying the of var

    hidden_2_layer = {'weights' : tf.Variable(tf.random_normal([n_node_hl1, n_node_hl2])),
                      'biases' : tf.Variable(tf.random_normal([n_node_hl2]))} 

    hidden_3_layer = {'weights' : tf.Variable(tf.random_normal([n_node_hl2, n_node_hl3])),
                      'biases' : tf.Variable(tf.random_normal([n_node_hl3]))} 

    output_layer = {'weights' : tf.Variable(tf.random_normal([n_node_hl3, n_classes])),
                    'biases' : tf.Variable(tf.random_normal([n_classes]))}

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']) + hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']) + hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)
    
    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']) + hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3, output_layer['weights']) + output_layer['biases'])
    return output


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction, y))
    optimizer = tf.train.AdagradOptimizer().minimize(cost)

    # cycles of feed forward + backprop
    hm_epoch = 10

    with tf.Session as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in hm_epoch:
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples / batch_size)):
                x, y = mnist.train.next_batch(batch_size)



# Main entry point of the program
if __name__ == "__main__":
    pass