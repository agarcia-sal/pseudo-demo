def is_prime(n: int) -> bool:
    # Return False for numbers less than 2
    if n < 2:
        return False

    # Only need to check divisors up to sqrt(n)
    limit = int(n**0.5) + 1
    for k in range(2, limit):
        if n % k == 0:
            return False

    return True