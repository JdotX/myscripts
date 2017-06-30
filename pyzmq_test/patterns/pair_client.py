import zmq, random, sys, time

port = "15001"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://192.168.2.103:5556")

while True:
    socket.send("client message to server1")
    msg = socket.recv()
    print msg

    time.sleep(1)
