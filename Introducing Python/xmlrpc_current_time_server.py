###########################################################
## Things to do 11.3
## "Use [XMLRPC] to implement a current-time-service.
##  When a client sends the string time to the server, 
##  return the current date and time as an ISO string."
###########################################################

from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

def curr_time(input):
    now = datetime.now()
    if input == "time":
        return now.isoformat()

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(curr_time, "curr_time")
server.serve_forever()
        