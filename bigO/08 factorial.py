#!/usr/bin/python

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# ⇒ O(n)
