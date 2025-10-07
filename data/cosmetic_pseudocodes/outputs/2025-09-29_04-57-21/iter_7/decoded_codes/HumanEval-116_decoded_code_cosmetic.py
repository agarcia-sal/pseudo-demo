from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted_list: List[int] = sorted(array_of_integers)
    # Sort by the count of '1' in binary representation (without '0b' prefix)
    result_list: List[int] = sorted(temp_sorted_list, key=lambda item: bin(item)[2:].count('1'))
    return result_list