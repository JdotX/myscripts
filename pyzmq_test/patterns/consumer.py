import time, zmq, random

def consumer():
    consumer_id = random.randrange(1,10005)
    print "I am consumer #%s" % (consumer_id)
    context = zmq.Context()

    consumer_rec = context.socket(zmq.PULL)
    consumer_rec.connect("tcp://127.0.0.1:15000")
    consumer_send = context.socket(zmq.PUSH)
    consumer_send.connect("tcp://127.0.0.1:15001")

    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = { 'consumer' : consumer_id, 'num' : data}
        if data%2 == 0:
            consumer_sender.send_json(result)

    return

consumer()
                                        
