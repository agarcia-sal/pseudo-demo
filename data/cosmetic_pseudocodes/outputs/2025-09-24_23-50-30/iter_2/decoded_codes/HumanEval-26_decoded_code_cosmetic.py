from typing import List
from collections import Counter

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: Counter[int] = Counter()
    for number in list_of_numbers:
        if counts[number] == 0:
            counts[number] = 1
        else:
            counts[number] += 1
    result: List[int] = []
    i: int = 0
    while i < len(list_of_numbers):
        if counts[list_of_numbers[i]] > 1:
            i += 1
            continue
        result.append(list_of_numbers[i])
        i += 1
    return result