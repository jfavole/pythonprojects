###########################################################
## Things to do 11.4
## "Write a simulation that pushes different types of
##  chocolate to a Redis list, and Lucy is a client
##  doing blocking pops of this list. She needs 0.5
##  seconds to handle a piece of chocolate. Print the time
##  and type of each chocolate as Lucy gets it, and how
##  many remain to be handled."
###########################################################

def lucy():
    import redis
    import time
    from datetime import datetime
    
    conn = redis.Redis()
    timeout = 20
    print('Lucy is ready.')
    
    while True:
        msg = conn.blpop('chocolates', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('One piece %s received at' % val, datetime.now())
        time.sleep(0.5)
    print('Lucy is finished.')

import multiprocessing

WORKERS = 2 ## Lucy and Ethel
for num in range(WORKERS):
    p = multiprocessing.Process(target=lucy)
    p.start()