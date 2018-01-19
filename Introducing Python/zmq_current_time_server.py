###########################################################
## Things to do 11.2
## "Use ZeroMQ REQ and REP sockets to [implement a current-
##  time-service. When a client sends the string time to 
##  the server, return the current date and time as an ISO
##  string.]"
###########################################################

import zmq
from datetime import datetime

## Establish connection
host = '127.0.0.1' ## Loopback address
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP) ## Synchronous reply socket
server.bind("tcp://%s:%s" % (host,port))

## Reply
now = datetime.now()
current_dt = bytes(now.isoformat(), 'utf-8')
request_bytes = server.recv()
request_str = request_bytes.decode('utf-8')
print("Client request: %s" % request_str)
server.send(current_dt)