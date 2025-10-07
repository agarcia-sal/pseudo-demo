from typing import List


def pairs_sum_to_zero(array_numbers: List[int]) -> bool:
    posA: int = 0
    length: int = len(array_numbers)
    while posA < length:
        posB: int = posA + 1
        while posB < length:
            sum_val: int = array_numbers[posA] + array_numbers[posB]
            if sum_val == 0:
                return True
            posB += 1
        posA += 1
    return False