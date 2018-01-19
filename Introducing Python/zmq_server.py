import zmq

## Set up connection information
host = '127.0.0.1' ## Loopback address
port = 6789
context = zmq.Context() ## ZeroMQ object that maintains state
server = context.socket(zmq.REP) ## Synchronous reply socket
server.bind("tcp://%s:%s" % (host, port))

## Reply
while True:
    ## Wait for the next request from client
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')
    print("That voice in my head says: %s" % request_str)
    reply_str = "Stop saying: %s" % request_str
    reply_bytes = bytes(reply_str, 'utf-8')
    server.send(reply_bytes)