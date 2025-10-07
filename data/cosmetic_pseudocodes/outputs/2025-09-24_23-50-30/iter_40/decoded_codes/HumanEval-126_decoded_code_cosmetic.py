from collections import Counter
from typing import Collection

def is_sorted(numbers_collection: Collection[int]) -> bool:
    frequency_map = Counter(numbers_collection)
    for i in range(len(numbers_collection)):
        if frequency_map[numbers_collection[i]] > 2:
            return False
    index = 1
    while index < len(numbers_collection):
        if not (numbers_collection[index - 1] <= numbers_collection[index]):
            return False
        index += 1
    return True