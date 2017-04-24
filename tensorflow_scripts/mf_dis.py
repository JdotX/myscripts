'''
Distributed matrix factorization v0.1
Not splitting the original matrix
24-Apr-2017
'''

from __future__ import division
import tensorflow as tf
import numpy as np
import time
import nmftool

parameter_servers = ["10.40.2.203:12301"]
workers = ["10.40.2.202:12201"]
#parameter_servers = ["10.40.199.203:12301"]
#workers = ["10.40.199.202:12201"]
proto = 'grpc'
cluster = tf.train.ClusterSpec({"ps": parameter_servers,
                                "worker": workers})

tf.app.flags.DEFINE_string("job_name", "", "Either 'ps' or 'worker'.")
tf.app.flags.DEFINE_integer("task_index", 0, "Index of task within the job")
FLAGS = tf.app.flags.FLAGS
server = tf.train.Server(cluster, job_name = FLAGS.job_name,
                         task_index = FLAGS.task_index,
                         protocol = proto)

learning_rate = 0.001
training_epochs = 10
rank = 1000
INFTY=1e12

def main():
    if FLAGS.job_name == "ps":
        server.join()
    elif FLAGS.job_name == "worker":
        with tf.device(tf.train.replica_device_setter(
                worker_device="/job:worker/task:%d" % FLAGS.task_index,
                cluster=cluster)):
            global_step = tf.get_variable('global_step', [],
                                          initializer=tf.constant_initializer(0),
                                          trainable=False)
            
            with tf.name_scope('input'):
                # read the input v
                V = np.random.rand(10000,10000)
                shape = V.shape
                scale = 2*np.sqrt(V.mean() / rank)
                H = tf.get_variable("H", [rank,shape[1]],
                                    initializer=tf.random_uniform_initializer(maxval=scale))
                W = tf.get_variable("W", [shape[0], rank],
                                    initializer=tf.random_uniform_initializer(maxval=scale))

            with tf.name_scope('step_eval'):
                WH = tf.matmul(W,H)
                forbenius_norm=tf.reduce_sum(tf.pow(V-WH,2))
                nn_w = tf.reduce_sum(tf.abs(W)-W)
                nn_h = tf.reduce_sum(tf.abs(H)-H)
                constraint=INFTY*(nn_w+nn_h)

            with tf.name_scope('step_loss'):
                step_loss = forbenius_norm + constraint

            with tf.name_scope('train'):
                train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(step_loss)    
            
        sv = tf.train.Supervisor(is_chief=(FLAGS.task_index==0),
                                 global_step=global_step)
        start_time=time.time()
        with sv.prepare_or_wait_for_session(server.target) as sess:
            f = open("mf_" + proto + str(len(workers)) + "w_" + str(FLAGS.task_index),  'w')
            sv.start_queue_runners(sess)
            for epoch in range(training_epochs):
                sess.run([train_step, step_loss, global_step])
                elapsed_time = time.time()-start_time
                start_time = time.time()
                print (elapsed_time)
                f.write(str(elapsed_time)+",")
        sv.stop()
        print("Distributed matrix factorization on this machine finished")

if __name__ == '__main__':
    main()
    

    
