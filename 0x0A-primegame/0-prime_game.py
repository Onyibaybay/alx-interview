#!/usr/bin/python3
"""
Prime game between Maria and Ben
"""


def is_prime(num):
    """Return True if num is a prime number, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_sieve(n):
    """Generate a list that marks primes up to n using the
    Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def prime_count_up_to(n, sieve):
    """Return the number of primes up to and including n using a sieve."""
    return sum(sieve[:n+1])


def isWinner(x, nums):
    """
    Determine the winner after x rounds.
    Maria plays first in each round.

    x: number of rounds
    nums: list of integers representing the upper limit of each round
    """
    if not nums or x < 1:
        return None

    # Generate primes up to the maximum number in nums
    max_n = max(nums)
    sieve = generate_prime_sieve(max_n)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers up to n
        primes_count = prime_count_up_to(n, sieve)

        # If the number of primes is odd, Maria wins (since she plays first)
        # If it's even, Ben wins (he will play last)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
