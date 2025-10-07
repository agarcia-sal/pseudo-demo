from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    tally: Counter[int] = Counter(list_of_numbers)
    result_list: List[int] = []
    iterator_position: int = 0

    while iterator_position < len(list_of_numbers):
        current_item: int = list_of_numbers[iterator_position]
        if tally[current_item] <= 1:
            result_list.append(current_item)
        iterator_position += 1

    return result_list