###########################################################
## Things to do 11.5
## "Use ZeroMQ to publish the poem from exercise 7.7,
##  one word at a time. Write a ZeroMQ consumer that prints
##  every word that starts with a vowel, and another that
##  prints every word that contains five letters. Ignore
##  punctuation characters."
###########################################################

import zmq
import re
import time
import string

## Establish connection settings.
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))

## Poem to be published.
poem = '''
    We have seen thee, queen of cheese,
    Lying quietly by your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare sieze.
    '''

time.sleep(1)

for word in poem.split():
    word = word.strip(string.punctuation)
    data = word.encode('utf-8')
    pat = r'\b[aeiou]\w*'
    vowels = re.findall(pat, poem)
    if vowels:
        pub.send_multipart([b'vowels', data])
    if len(word) == 5:
        pub.send_multipart([b'fives', data])