from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    ascending_sorted_array: List[int] = sorted(array_of_integers)
    # Sort by number of '1's in binary representation, stable sort keeps ascending order among equal counts
    sorted_by_binary_ones: List[int] = sorted(
        ascending_sorted_array,
        key=lambda element: bin(element).count('1')
    )
    return sorted_by_binary_ones