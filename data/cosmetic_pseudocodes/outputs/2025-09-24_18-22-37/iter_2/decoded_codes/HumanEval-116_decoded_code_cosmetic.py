from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    ascending_sorted: List[int] = sorted(array_of_integers)
    # Sort by number of '1's in binary representation
    result: List[int] = sorted(
        ascending_sorted,
        key=lambda elem: bin(elem).count('1')
    )
    return result