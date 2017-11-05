import tensorflow as tf

'''
In TensorFlow, data isn't stored as integers,floats or strings. These values are encapsulated in an object called a
tensor.

In the case of hello_constant = tf.constant('Hello World!'), hello_constant is a 0-dimensional string tensor, but tensors
 come in a  variety of size:

# A is a 0-dimensional int32 tensor
A = tf.constant(1234)
# B is a 1-dimensional int32 tensor
B = tf.constant([123, 456, 789])
# C is a 2-dimensional int32 tensor
C = tf.constant([123, 456, 789], [222, 333, 444])

Pass a non-constant
tf.placeholder() returns a tensor that get its value from data passed to the tf.session.run() function, allowing us to
set the input right before the session runs

feed_dict parameter in tf.session.run() is use to set the placeholder tensor.

'''
# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)

