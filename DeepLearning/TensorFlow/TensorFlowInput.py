import tensorflow as tf

'''
Pass a non-constant
tf.placeholder() returns a tensor that get its value from data passed to the tf.session.run() function, allowing us to
set the input right before the session runs

feed_dict parameter in tf.session.run() is use to set the placeholder tensor.

'''


def run():
    output = None
    x = tf.placeholder(tf.int32)

    with tf.Session() as sess:
        output = sess.run(x, feed_dict={x: 123})
    return output


if __name__ == "__main__":
    value = run()
    print(value)
