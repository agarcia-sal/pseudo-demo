from typing import List


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        # Check divisibility up to sqrt(k) for efficiency
        limit = int(k**0.5) + 1
        return all(k % i != 0 for i in range(2, limit))

    result_accumulator: int = 1
    divisor_candidates: List[int] = list(range(2, n))
    index_tracker: int = 0
    while index_tracker < len(divisor_candidates):
        current_divisor = divisor_candidates[index_tracker]
        if n % current_divisor == 0 and is_prime(current_divisor):
            if current_divisor > result_accumulator:
                result_accumulator = current_divisor
        index_tracker += 1
    return result_accumulator