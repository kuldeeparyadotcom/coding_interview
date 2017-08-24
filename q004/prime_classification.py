#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def classify_list(l):
    """
        Purpose - function classifies prime numbers vs non-prime numbers
        Input - a list of positive integers
        Ouput - For each number in list, program confirms whether it is prime or not
    """
    for n in l: #Traverse through the given list
        is_prime = True
        first_divisor = 1 #default initialization
        remainder_by_first_divisor = 1 #Default initialization
        for d in range(2,n): #See if number n is devisible by any number other than 1 and itself
            if n % d == 0: #number n is divisible by d that is neither 1 nor number n
                is_prime = False
                first_divisor = d
                remainder_by_first_divisor = n // d
                break
        if is_prime:
            print(n, "is a prime number")
        else:
            print(n, "is not a prime number", n,"=",first_divisor,"*",remainder_by_first_divisor)
    else:
        print("Classification complete!!!")


#Test it locally
if __name__ == "__main__":
    classify_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
