from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: Counter[int] = Counter(list_of_numbers)
    return [element for element in list_of_numbers if counts[element] <= 1]