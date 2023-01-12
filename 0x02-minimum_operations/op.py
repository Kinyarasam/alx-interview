#!/usr/bin/python3
import math


def is_prime(n):
    if n < 2 and n > 0:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def minOperationis(n):
    """
    Calculate the minimum number of operations needed to result in exactly n
    H characters in the file

    Args:
        n (int): The number of H characters

    Returns:
        (int): The minimum number of operations needed.
        If n is impossible to achieve, return 0.
    """
    # Initialize dp with 0's and return 0 if n is <= 0
    if n <= 0:
        return 0

    dp = [0] * (n + 1)
    # Iterate through each number of H's
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        j = 2
        # Iterate through multiples of H's
        while j * i <= n:
            dp[j * i] = min(dp[j * i], dp[i] + j - 1)
            j += 1
    # Return the minimum number of operations needed to reach n H's
    return dp[n]

def HasRoot(n):
    root = math.sqrt(n)
    if ((root - int(root)) == 0):
        return True
    else:
        return False

def minOperations(n):
    if isinstance(n, int):
        print(HasRoot(n))
        print('isPrime {}'.format(is_prime(n)))
