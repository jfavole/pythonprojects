"""
Tiny program to learn how to measure timing for code optimization (timeit).
"""

from timeit import timeit
print(timeit('num = 5; num *= 2', number=1))