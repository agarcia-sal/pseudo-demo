from typing import List
from collections import Counter

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    element_frequencies: Counter[int] = Counter(list_of_numbers)
    unique_number_list: List[int] = []
    position: int = 0
    while position < len(list_of_numbers):
        current_value: int = list_of_numbers[position]
        if not (element_frequencies[current_value] > 1):
            unique_number_list.append(current_value)
        position += 1
    return unique_number_list