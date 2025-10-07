from typing import List

def pairs_sum_to_zero(array_param: List[int]) -> bool:
    length = len(array_param)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if array_param[i] + array_param[j] == 0:
                return True
            j += 1
        i += 1
    return False