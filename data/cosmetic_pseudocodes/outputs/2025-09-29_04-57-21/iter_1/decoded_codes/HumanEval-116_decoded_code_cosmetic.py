from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted: List[int] = sorted(array_of_integers)
    # Sort by number of '1's in the binary representation of each item
    result: List[int] = sorted(temp_sorted, key=lambda item: bin(item).count('1'))
    return result