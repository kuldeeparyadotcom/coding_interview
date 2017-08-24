#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def print_fibo_till_n(n):
    """
        Purpose -  prints fibonacci series until fibonacci number is less than the given number n
    """
    a, b = 0, 1 #Initialize first two fibonacci numbers
    while (b < n):
        print(b)
        a, b = b, a+b

if __name__ == "__main__":
    n = int(input("Enter the positive integer to limit fibonacci series printing"))
    print_fibo_till_n(n)

