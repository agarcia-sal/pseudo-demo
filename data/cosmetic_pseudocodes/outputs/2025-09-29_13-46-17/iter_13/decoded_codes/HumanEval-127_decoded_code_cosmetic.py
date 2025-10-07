from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        # Helper recursive function to check primality by trial division starting at j=2
        def check_prime(m: int, j: int = 2) -> bool:
            if m == 0 or m == 1:
                return False
            if j == 2 and m != 0 and m != 1:
                if j > m // 2:
                    return True  # No divisor found upto m//2
            if j > m // 2:
                return True  # no divisor found
            if m % j == 0:
                return False
            return check_prime(m, j + 1)

        return check_prime(number, 2)

    def compute(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
        left_ep = interval1[0] if interval1[0] >= interval2[0] else interval2[0]
        right_ep = interval1[1] if interval1[1] <= interval2[1] else interval2[1]
        length = right_ep - left_ep
        return "YES" if length > 0 and is_prime(length) else "NO"

    return compute(interval1, interval2)