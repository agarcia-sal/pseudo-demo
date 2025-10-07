from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    # Sort by element value ascending
    sorted_by_value = sorted(array_of_integers)
    # Sort by count of '1's in binary representation (excluding first character 'b')
    sorted_final = sorted(
        sorted_by_value,
        key=lambda x: bin(x)[2:].count('1')
    )
    return sorted_final