import zmq

## Set up connection information
host = '127.0.0.1' ## Loopback address
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ) ## Synchronous request socket
client.connect("tcp://%s:%s" % (host, port))

## Request
for num in range(1, 6):
    request_str = "message #%s" % num
    request_bytes = request_str.encode('utf-8')
    client.send(request_bytes)
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode('utf-8')
    print("Sent %s, received %s" % (request_str, reply_str))