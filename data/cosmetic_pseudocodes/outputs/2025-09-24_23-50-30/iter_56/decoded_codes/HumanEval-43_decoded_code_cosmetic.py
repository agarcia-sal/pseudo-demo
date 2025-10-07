from typing import List

def pairs_sum_to_zero(array_integers: List[int]) -> bool:
    current_index: int = 0
    length: int = len(array_integers)
    while current_index < length - 1:
        search_index: int = current_index + 1
        while search_index < length:
            # Check if sum of the pair is zero
            if not ((array_integers[current_index] + array_integers[search_index]) != 0):
                return True
            search_index += 1
        current_index += 1
    return False