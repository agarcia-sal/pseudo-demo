from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    array_sorted_by_value = sorted(array_of_integers)
    array_sorted_by_number_of_ones = sorted(array_sorted_by_value, key=lambda x: bin(x).count('1'))
    return array_sorted_by_number_of_ones