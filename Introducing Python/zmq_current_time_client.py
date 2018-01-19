###########################################################
## Things to do 11.2
## "Use ZeroMQ REQ and REP sockets to [implement a current-
##  time-service. When a client sends the string time to 
##  the server, return the current date and time as an ISO
##  string.]"
###########################################################

import zmq

## Establish connection
host = '127.0.0.1' ## Loopback address
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ) ## Synchronous request socket
client.connect("tcp://%s:%s" % (host, port))

## Request
request_str = "time"
request = bytes(request_str, 'utf-8')
client.send(request)
reply_bytes = client.recv()
reply_str = reply_bytes.decode('utf-8')
print("The current time is: %s" % reply_str)