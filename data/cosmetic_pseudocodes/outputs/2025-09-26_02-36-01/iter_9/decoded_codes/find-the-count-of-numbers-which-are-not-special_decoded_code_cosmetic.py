import math

class Solution:
    def nonSpecialCount(self, x: int, y: int) -> int:
        def is_prime(z: int) -> bool:
            def check_factors(m: int) -> bool:
                if m * m > z:
                    return True
                if (z % m == 0) or (z % (m + 2) == 0):
                    return False
                return check_factors(m + 6)

            if z <= 1:
                return False
            if z <= 3:
                return True
            if (z % 2 == 0) or (z % 3 == 0):
                return False
            return check_factors(5)

        min_prime_candidate = math.ceil(math.sqrt(x))
        max_prime_candidate = math.floor(math.sqrt(y))

        special_counter = 0

        def count_primes_in_range(current: int, limit: int) -> None:
            nonlocal special_counter
            if current > limit:
                return
            if is_prime(current):
                special_counter += 1
            count_primes_in_range(current + 1, limit)

        count_primes_in_range(min_prime_candidate, max_prime_candidate)

        range_total = (y - x) + 1

        return range_total - special_counter