#!/usr/bin/python3
"""Change comes from within module
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet the given amount.

    Args:
        coins (List): List of values of the coins in your possession.
        total (int): The total amount which you need to make change.

    Returns:
        (int) - The fewest number of coins needed to meet total
    """
    if total < 1:
        return 0

    # Initialize the dynamic programming table.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the dynamic programming table
    for i in range(1, total + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    # return the result
    return dp[total] if dp[total] != float('inf') else -1
