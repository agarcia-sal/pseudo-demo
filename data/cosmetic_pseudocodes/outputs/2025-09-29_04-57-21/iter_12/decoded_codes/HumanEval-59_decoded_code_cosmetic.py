def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for divisor_candidate in range(2, k):
            if k % divisor_candidate == 0:
                return False
        return True

    max_factor = 1
    potential_divisor = 2
    while potential_divisor <= n:
        if n % potential_divisor == 0:
            if is_prime(potential_divisor):
                if max_factor < potential_divisor:
                    max_factor = potential_divisor
        potential_divisor += 1
    return max_factor