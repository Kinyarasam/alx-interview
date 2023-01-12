#!/usr/bin/python3
import math


def isPrime(numb):
    """Check if number is a prime number

    Returns:
        (Bool): True or false
    """
    if numb <= 1:
        return False
    for x in range(2, int(numb**(1/2))+1):
        if numb % x == 0:
            return False
    return True

def getFactors(numb):
    """Get all the factors of a number

    Returns:
        (List[int]): The factors of a number
    """
    factors = []
    for x in range(1, numb+1):
        if numb % x == 0:
            factors.append(x)
    return factors

def isPerfectSquare(numb):
    """Check if a number is a square

    Args:
        numb (int): The number to check.

    Return:
        (bool): True or false.
    """
    if numb < 0:
        return False
    elif math.isqrt(numb)**2 == numb:
        return True
    return False

def getMidPoint(n):
    lst = getFactors(n)
    print(lst)
    mid = int(len(lst) / 2)
    print(lst[mid])
    print(isPerfectSquare(mid))

    if (len(lst) % 2 == 0):
        return (lst[mid] + lst[mid - 1])
    else:
        return (lst[mid] * 2)

def minOperations(n):
    """main function"""
    #if (isPrime(n)):
    #    return n
    return getMidPoint(n)
