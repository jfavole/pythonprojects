"""
Tiny program to learn how to measure timing for code optimization.
"""

from time import time

t1 = time()
num = 5
num *= 2
print(time() - t1)