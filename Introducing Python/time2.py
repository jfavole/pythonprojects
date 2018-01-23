"""
Tiny program to learn how to measure timing for code optimization.
"""

from time import time, sleep

t1 = time()
sleep(1.0)
print(time() - t1)