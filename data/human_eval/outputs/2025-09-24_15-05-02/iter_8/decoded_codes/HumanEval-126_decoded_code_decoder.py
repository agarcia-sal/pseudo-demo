from typing import List
from collections import Counter

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_occurrences = Counter(list_of_numbers)
    if any(count > 2 for count in count_occurrences.values()):
        return False
    return all(
        list_of_numbers[i - 1] <= list_of_numbers[i]
        for i in range(1, len(list_of_numbers))
    )