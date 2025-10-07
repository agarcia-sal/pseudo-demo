from typing import Tuple

def intersection(rangeA: Tuple[int, int], rangeB: Tuple[int, int]) -> str:
    def is_prime(val: int) -> bool:
        if val in (0, 1):
            return False
        if val == 2:
            return True
        for divisor in range(2, val):
            if val % divisor == 0:
                return False
        return True

    start_val = rangeA[0] if rangeA[0] > rangeB[0] else rangeB[0]
    end_val = rangeA[1] if rangeA[1] < rangeB[1] else rangeB[1]
    length_val = end_val - start_val
    if length_val > 0 and is_prime(length_val):
        return "YES"
    return "NO"