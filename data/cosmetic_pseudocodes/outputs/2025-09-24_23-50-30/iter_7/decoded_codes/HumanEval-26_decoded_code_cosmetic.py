from collections import Counter
from typing import List, Sequence

def remove_duplicates(numbers_collection: Sequence[int]) -> List[int]:
    frequency_map = Counter(numbers_collection)

    def filter_unique(index: int, acc: List[int]) -> List[int]:
        if index == len(numbers_collection):
            return acc
        current_item = numbers_collection[index]
        if frequency_map[current_item] > 1:
            return filter_unique(index + 1, acc)
        return filter_unique(index + 1, acc + [current_item])

    return filter_unique(0, [])