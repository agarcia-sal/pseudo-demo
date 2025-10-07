from typing import List

def pairs_sum_to_zero(numbers: List[int]) -> bool:
    index_outer: int = 0
    length: int = len(numbers)
    while index_outer < length:
        current_value: int = numbers[index_outer]
        index_inner: int = index_outer + 1
        while index_inner < length:
            if numbers[index_inner] == -current_value:
                return True
            index_inner += 1
        index_outer += 1
    return False