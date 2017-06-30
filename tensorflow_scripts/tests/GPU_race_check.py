# This scripts aims to test the TF under development's race conditions
# i.e. whether read and write to GPU is taking place at the same time
# Jiacheng Xia, 19-6-2017

import os, portpicker, subprocess, sys, threading, time
import tensorflow as tf


'''
' Define constants
'''=
flags=tf.flags
flags.DEFINE_integer("iters", 10, "No. of asynchronous iterations")
flags.DEFINE_integer("data_mb", 128, "size of 1D tensor in MBs")
flags.DEFINE_string("task_index", "", "No. of current task")
flags.DEFINE_string("port0", "12222", "port of worker1, used as master")
flags.DEFINE_string("port1", "12223", "port of worker2")
flags.DEFINE_boolean("verbose", False, "whether to have verbose logging")
flags.DEFINE_boolean("profile", False, "whether to collect CPU profile")
flags.DEFINE_boolean("use_gpu", False, "Whether to use GPU transfer")
FLAGS = flags.FLAGS

host = "127.0.0.1"

'''
' Initialize functions.
'''
def session_config():
    optimizer_options = tf.OptimizerOptions(opt_level=tf.OptimizerOptions.L0)
    graph_oprions = tf.GraphOptions(optimizer_options=optimizer_options)
    config = tf.ConfigProto(graph_options=graph_options,
                            intra_op_parallelism_threads=10,
                            inter_op_parallelism_threads=10)

def cluster_spec():
    tf_cluster = {"worker": [host+":"+FLAGS.port0, host+":"+FLAGS.port1]}
    return tf.train.ClusterSpec(tf_cluster).as_cluster_def()


def create_graph(device0, device1):
    tf.reset_default_graph()
    dtype=tf.int32
    params_size = 250*1000*FLAGS.data_mb # 1MB is 250k integers
  
    with tf.device(device0):
        var1 = tf.get_variable("var1", [params_size], dtype,
                               initializer=tf.ones_initializer())
    with tf.device(device1):
        var2 = tf.get_variable("var2", [params_size], dtype,
                               initializer=tf.ones_initializer())

    add_op = tf.add(var1, var2)
    init_op = tf.global_variables_initializer()
    return init_op, add_op

    
def run_benchmark(sess, init_op, add_op):
    sess.run(init_op)
    for _ in range(10):
        sess.run(add_op.op)
    start_time = time.time()
    for i in range(FLAGS.iters):
        sess.run(add_op.op)

    elapsed_time = time.time() - start_time
    return float()


            
