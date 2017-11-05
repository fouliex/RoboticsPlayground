import tensorflow as tf

'''
Implement and print the cross entropy when given a set of softmax values,
and corresponding one-hot encoded labels.

tf.reduce_sum() function takes an array of numbers and sums them together.
tf.log() takes the natural lof oa number
'''
softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# Print cross entropy from session
cross_entropy = - tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

with tf.Session() as sess:
    print(sess.run(cross_entropy, feed_dict={softmax: softmax_data, one_hot: one_hot_data}))
