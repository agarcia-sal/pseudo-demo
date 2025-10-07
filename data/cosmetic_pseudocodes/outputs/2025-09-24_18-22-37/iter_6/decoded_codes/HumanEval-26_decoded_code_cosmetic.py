from collections import Counter
from typing import List

def remove_duplicates(numbers_list: List[int]) -> List[int]:
    tally: Counter[int] = Counter(numbers_list)
    unique_elements: List[int] = []
    index: int = 0
    while index < len(numbers_list):
        current_item: int = numbers_list[index]
        if tally[current_item] <= 1:
            unique_elements.append(current_item)
        index += 1
    return unique_elements