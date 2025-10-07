from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    # Sort by integer value ascending
    sorted_by_value = sorted(array_of_integers)
    # Then sort by count of ones in the binary representation ascending (stable sort)
    return sorted(sorted_by_value, key=lambda x: bin(x).count('1'))