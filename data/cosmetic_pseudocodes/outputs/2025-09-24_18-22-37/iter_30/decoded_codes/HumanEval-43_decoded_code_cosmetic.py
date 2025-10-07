from typing import List

def pairs_sum_to_zero(array_of_numbers: List[int]) -> bool:
    p: int = 0
    length: int = len(array_of_numbers)
    while p < length:
        q: int = p + 1
        while q < length:
            sum_check: int = array_of_numbers[p] + array_of_numbers[q]
            if sum_check == 0:
                return True
            q += 1
        p += 1
    return False