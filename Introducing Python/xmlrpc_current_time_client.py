###########################################################
## Things to do 11.3
## "Use [XMLRPC] to implement a current-time-service.
##  When a client sends the string time to the server, 
##  return the current date and time as an ISO string."
###########################################################

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")

current_time = proxy.curr_time('time')
print("Current time is:", current_time)

