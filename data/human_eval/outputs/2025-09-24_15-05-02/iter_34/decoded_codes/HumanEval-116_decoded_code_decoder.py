from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    sorted_array_based_on_decimal: List[int] = sorted(array_of_integers)
    final_sorted_array: List[int] = sorted(sorted_array_based_on_decimal, key=lambda element: bin(element).count('1'))
    return final_sorted_array