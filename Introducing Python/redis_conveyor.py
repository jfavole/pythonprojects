###########################################################
## Things to do 11.4
## "Write a simulation that pushes different types of
##  chocolate to a Redis list, and Lucy is a client
##  doing blocking pops of this list. She needs 0.5
##  seconds to handle a piece of chocolate. Print the time
##  and type of each chocolate as Lucy gets it, and how
##  many remain to be handled."
###########################################################

import redis

conn = redis.Redis()
print('Conveyor belt is starting.')

chocolates = ['dark truffle', 'milk truffle', 'cherry cordial', 'caramel']

for chocolate in chocolates:
    msg = chocolate.encode('utf-8')
    conn.rpush('chocolates', msg)
    print('Sending', chocolate, 'down the belt.')
conn.rpush('chocolates', 'quit')
print('No more chocolates to send.')
