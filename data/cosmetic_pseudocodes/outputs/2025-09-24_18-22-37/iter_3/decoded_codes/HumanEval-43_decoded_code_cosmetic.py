from typing import List

def pairs_sum_to_zero(numbers: List[int]) -> bool:
    length: int = len(numbers)
    idx1: int = 0
    while idx1 < length:
        idx2: int = idx1 + 1
        while idx2 < length:
            if numbers[idx1] + numbers[idx2] == 0:
                return True
            idx2 += 1
        idx1 += 1
    return False