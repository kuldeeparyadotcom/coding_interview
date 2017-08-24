#!/usr/bin/env python

# vim: tabstop=8 expandtab shifttab=4 softtabstop=4

"""
    Purpose - To print fibonacci number until fobonacci number is less than the given limit
    Implementation Approach - recursion
"""

def print_fibo_till_n(n):
    """
        method signature: print_fibo_till_n(n)
        Input - positive interger n to stop the fibonacci printing
        output - prints fibonacci series until given limit on attached standar output
    """
    a, b = 0, 1 #Initialize first two fibonacci numbers
    print_fibo(a, b, n) #Call recursive helper method

def print_fibo(a, b, n): #Helper method for print_fibo_till_n(n)
    if (b < n):
        print(b)
        print_fibo(b, a+b, n)

if __name__ == "__main__":
    n = int(input("Please enter a positive integer to limit fobo series: "))
    print_fibo_till_n(n)
