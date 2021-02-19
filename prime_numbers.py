"""
Usage example: Find all the primes up to 1 million.
$ python prime_numbers.py 1000000
"""

#!/usr/bin/env python
# coding: utf-8

from time import time
from math import sqrt
import functools
import sys

max_cache_size=1024

@functools.lru_cache(maxsize=max_cache_size)
def is_prime(number):
    if number==1:
        return False
    if number==2:
        return True
    divisor=2
    while divisor <= sqrt(number):
        if number%divisor == 0:
            return False
        divisor=next_prime(divisor)
    return True

@functools.lru_cache(maxsize=max_cache_size)
def next_prime(number):
    if number==1:
        return 2
    if number==2:
        return 3
    if is_prime(number+1):
        return number+1
    return next_prime(number+1)


def primes(cutoff):
    i=1
    number=2
    while number <= cutoff:
        print(f'{i}:   {number}')
        number=next_prime(number)
        i+=1

if __name__ == '__main__':
    cutoff=int(sys.argv[1])
    start=time()
    primes(cutoff)
    end=time()
    print(f'\nExecution time: {end-start} seconds.')