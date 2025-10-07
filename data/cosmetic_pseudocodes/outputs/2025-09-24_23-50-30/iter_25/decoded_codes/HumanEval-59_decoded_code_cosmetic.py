def largest_prime_factor(m: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        for q in range(2, p):
            if p % q == 0:
                return False
        return True

    max_factor: int = 1
    r: int = 2
    while r <= m:
        if m % r == 0 and is_prime(r):
            if max_factor < r:
                max_factor = r
        r += 1
    return max_factor