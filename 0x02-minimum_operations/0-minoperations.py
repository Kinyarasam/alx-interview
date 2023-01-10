#!/usr/bin/python3
def minOperations(n):
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
