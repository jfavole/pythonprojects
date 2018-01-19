###########################################################
## Things to do 11.5
## "Use ZeroMQ to publish the poem from exercise 7.7,
##  one word at a time. Write a ZeroMQ consumer that prints
##  every word that starts with a vowel, and another that
##  prints every word that contains five letters. Ignore
##  punctuation characters."
###########################################################

import string
import zmq

## Establish connection settings.
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))

## Subscriber.
sub.setsockopt(zmq.SUBSCRIBE, b'vowels')
sub.setsockopt(zmq.SUBSCRIBE, b'fives')

while True:
    topic, word = sub.recv_multipart()
    print(topic, word)