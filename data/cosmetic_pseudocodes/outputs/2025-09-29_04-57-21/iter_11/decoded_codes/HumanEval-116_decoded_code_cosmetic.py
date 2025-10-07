from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    interim_array = sorted(array_of_integers)
    # Sort by count of '1's in binary representation after skipping '0b' prefix
    result_list = sorted(interim_array, key=lambda x: bin(x)[2:].count('1'))
    return result_list