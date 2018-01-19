###########################################################
## Things to do 11.1
## "Use a plain socket to implement a current-time-service.
##  When a client sends the string time to the server, 
##  return the current date and time as an ISO string."
###########################################################

import socket
import binascii
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000
now = datetime.now()
current_dt = bytes(now.isoformat(), 'utf-8')

print('Starting the server.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print('Client request:', data)

client.sendall(current_dt)
client.close()
server.close()