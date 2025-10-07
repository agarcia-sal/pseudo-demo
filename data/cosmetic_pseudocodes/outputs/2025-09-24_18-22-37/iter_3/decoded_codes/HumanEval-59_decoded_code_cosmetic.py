def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        divisor = 2
        while divisor < k:
            if k % divisor == 0:
                return False
            divisor += 1
        return True

    candidate = 2
    result = 1
    while candidate <= n:
        if n % candidate == 0:
            if is_prime(candidate) and candidate > result:
                result = candidate
        candidate += 1
    return result