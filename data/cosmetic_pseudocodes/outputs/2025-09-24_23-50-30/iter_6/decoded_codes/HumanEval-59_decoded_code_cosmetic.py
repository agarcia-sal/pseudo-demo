def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        divisor_counter = 2
        while divisor_counter < y:
            if y % divisor_counter == 0:
                return False
            divisor_counter += 1
        return True

    max_factor = 1
    candidate = 2
    while candidate <= x:
        if x % candidate == 0:
            if is_prime(candidate) and candidate > max_factor:
                max_factor = candidate
        candidate += 1
    return max_factor