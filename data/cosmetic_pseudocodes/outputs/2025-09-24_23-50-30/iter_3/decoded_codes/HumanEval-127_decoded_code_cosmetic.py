from typing import Sequence, Union


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    left_bound: int = interval1[0]
    if interval2[0] > left_bound:
        left_bound = interval2[0]

    right_bound: int = interval1[1]
    if interval2[1] < right_bound:
        right_bound = interval2[1]

    overlap: int = right_bound - left_bound
    if overlap > 0 and is_prime(overlap):
        return "YES"
    return "NO"