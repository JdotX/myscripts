'''
This is the testing script for Matrix Factorization using Tensorflow 
(single machine version)
Modified from "wide-n-deep" tutorial from official
21-Apr-2017
'''

from __future__ import division
import tensorflow as tf
import numpy as np
import time

'''
parameter_servers = ["10.40.2.203:12301"]
workers = ["10.40.2.202:12201",
           "10.40.2.201:12201",
           "10.40.2.200:12200"]

cluster = tf.train.ClusterSpec({"ps": parameter_servers,
                                "worker": workers})

tf.app.flags.DEFINE_string("job_name", "", "Either 'ps' or 'worker'.")
tf.app.flags.DEFINE_integer("task_index", 0, "Index of task within the job")
FLAGS = tf.app.flags.FLAGS
server = tf.train.Server(cluster, job_name = FLAGS.job_name,
                         task_index = FLAGS.task_index,
                         protocol = 'grpc')
'''

INFTY = 1e12

class NMF(object):
    def __init__ (self, V, rank, learning_rate = 0.01):
        self.V = tf.constant(V, dtype=tf.float32)
        shape = V.shape
        self.rank = rank
        self.lr = learning_rate

        scale = 2*np.sqrt(V.mean()/rank)
        initializer = tf.random_uniform_initializer(maxval=scale)
        self.H = tf.get_variable("H", [rank, shape[1]], initializer=initializer)
        self.W = tf.get_variable("W", [shape[0], rank], initializer=initializer)
        self._build_grad_algorithm()
        
    def _build_grad_algorithm(self):
        V,W,H = self.V, self.W, self.H
        WH = tf.matmul(W,H)
        forbenius_norm = tf.reduce_sum(tf.pow(V-WH, 2))

        # non-negative
        nn_w = tf.reduce_sum(tf.abs(W)-W)
        nn_h = tf.reduce_sum(tf.abs(H)-H)
        constraint = INFTY * (nn_w + nn_h)
        loss = forbenius_norm + constraint
        self.loss = loss 
        self.optimize = tf.train.GradientDescentOptimizer(self.lr).minimize(loss)

    def run(self, sess, max_iter = 2000, min_delta = 0.0001):
        tf.initialize_all_variables().run()
        return self._run_sgd(sess, max_iter, min_delta)

    def _run_sgd(self, sess, max_iter, min_delta):
        pre_loss = INFTY
        for i in xrange(max_iter):
            print ("iter no. " + str(i) + "\tpre loss " + str(pre_loss))
            loss, _ = sess.run([self.loss, self.optimize])
            print (loss)
            if abs(pre_loss - loss) < min_delta:
                break
            pre_loss = loss

        W = self.W.eval()
        H = self.H.eval()
        return W,H


def main():
    V = np.random.rand(3,3)
    rank = 10
    print(V)
    tf_nmf = NMF(V, rank)
    #config = tf.ConfigProto(inter_op_parallelis)
    with tf.Session() as sess:
        start = time.time()
        W,H = tf_nmf.run(sess)
        print (time.time()-start)

    W = np.mat(W)
    H = np.mat(H)
    print (W*H)
    err = np.power(V-W*H,2).sum()
    print ("Reconstruction error is ", err)

if __name__ == '__main__':
    main()
    

    
