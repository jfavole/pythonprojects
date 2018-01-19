import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000 ## Max acceptable message length

print('Starting the client at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## Streaming protocol, TCP
client.connect(address) ## Client connects to server
client.sendall(b'Hey!') ## Sends byte streams

data = client.recv(max_size)
print('At', datetime.now(), 'someone replied,', data)
client.close()