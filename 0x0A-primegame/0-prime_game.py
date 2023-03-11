#!/usr/bin/python3
"""Prime game
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with x rounds.

    Args:
        x (int): Number of rounds.
        nums (List): ...

    Returns:
        (str): winner.
    """
    if x < 1 or not nums:
        return None

    Maria_wins, Ben_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(1 + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0:n])))
        Ben_wins += primes_count % 2 == 0
        Maria_wins += primes_count % 2 == 1

    if Maria_wins == Ben_wins:
        return None

    winner = 'Maria' if Maria_wins > Ben_wins else 'Ben'

    return winner
