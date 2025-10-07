from typing import List
from collections import Counter

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: Counter[int] = Counter(list_of_numbers)
    return [element for element in list_of_numbers if counts[element] <= 1]