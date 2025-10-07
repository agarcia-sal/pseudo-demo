def largest_prime_factor(n: int) -> int:
    import math

    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k == 2:
            return True
        if k % 2 == 0:
            return False
        limit = int(math.sqrt(k)) + 1
        for i in range(3, limit, 2):
            if k % i == 0:
                return False
        return True

    largest = 1
    # Only need to check up to sqrt(n) to find factors
    limit = int(math.sqrt(n)) + 1
    for j in range(2, limit):
        if n % j == 0:
            # Check if j is prime
            if is_prime(j):
                largest = max(largest, j)
            # Check the paired factor n//j
            paired_factor = n // j
            if is_prime(paired_factor):
                largest = max(largest, paired_factor)

    # If no factor found and n > 1, n itself might be prime
    if largest == 1 and n > 1 and is_prime(n):
        largest = n

    return largest