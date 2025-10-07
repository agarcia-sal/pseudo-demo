from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts = Counter(list_of_numbers)

    def filter_unique(idx: int, acc: List[int]) -> List[int]:
        if idx == len(list_of_numbers):
            return acc
        current_element = list_of_numbers[idx]
        if counts[current_element] <= 1:
            acc = acc + [current_element]
        return filter_unique(idx + 1, acc)

    return filter_unique(0, [])