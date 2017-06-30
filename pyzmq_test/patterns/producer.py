import time, zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://192.168.2.103:15000")
    for num in xrange(10000):
        msg = {'num': num}
        zmq_socket.send_json(msg)
    return

producer()
