###########################################################
## Things to do 11.1
## "Use a plain socket to implement a current-time-service.
##  When a client sends the string time to the server, 
##  return the current date and time as an ISO string."
###########################################################

import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

client.sendall(b'time') ## Send time string to server
data = client.recv(max_size)

print('Current date and time are:', data)
client.close()