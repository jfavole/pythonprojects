"""
Tiny program to learn how to measure timing for code optimization (timeit).
"""

from timeit import repeat
print(repeat('num = 5; num *= 2', number=1, repeat=3))