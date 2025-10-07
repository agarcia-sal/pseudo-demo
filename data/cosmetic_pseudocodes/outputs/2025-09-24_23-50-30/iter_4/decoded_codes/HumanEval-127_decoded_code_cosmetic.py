from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> None:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        return all(n % i != 0 for i in range(2, n))

    left = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    right = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    length = right - left

    if length > 0 and is_prime(length):
        print("YES")
    else:
        print("NO")