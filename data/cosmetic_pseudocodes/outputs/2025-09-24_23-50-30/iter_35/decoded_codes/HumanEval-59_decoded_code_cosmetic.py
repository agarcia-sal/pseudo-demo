def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        idx = 2
        while idx * idx <= y:
            if y % idx == 0:
                return False
            idx += 1
        return True

    candidate = 2
    max_prime = 1
    while candidate <= x:
        if x % candidate == 0 and is_prime(candidate):
            if candidate > max_prime:
                max_prime = candidate
        candidate += 1

    return max_prime