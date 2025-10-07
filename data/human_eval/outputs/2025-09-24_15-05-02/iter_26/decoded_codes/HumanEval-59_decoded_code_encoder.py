from typing import Optional

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k == 2:
            return True
        if k % 2 == 0:
            return False
        # check odd divisors up to sqrt(k)
        limit = int(k**0.5) + 1
        for i in range(3, limit, 2):
            if k % i == 0:
                return False
        return True

    if n < 2:
        return 1  # no prime factors for numbers below 2

    largest = 1
    # check only factors up to sqrt(n) and their complementary factors
    limit = int(n**0.5) + 1
    for j in range(2, limit):
        if n % j == 0:
            if is_prime(j):
                if j > largest:
                    largest = j
            complement = n // j
            if complement != j and is_prime(complement):
                if complement > largest:
                    largest = complement
    return largest if largest != 1 else (n if is_prime(n) else 1)