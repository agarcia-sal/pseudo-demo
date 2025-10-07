from typing import Callable


def largest_prime_factor(magnitude: int) -> int:
    def is_prime(candidate: int) -> bool:
        if candidate < 2:
            return False
        divisor_candidate = 2
        while divisor_candidate < candidate:
            if candidate % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    def scan_divisors(current_factor: int, max_factor: int) -> int:
        if current_factor > max_factor:
            return 1
        next_largest = scan_divisors(current_factor + 1, max_factor)
        if magnitude % current_factor == 0 and is_prime(current_factor):
            return current_factor if current_factor > next_largest else next_largest
        return next_largest

    return scan_divisors(2, magnitude)