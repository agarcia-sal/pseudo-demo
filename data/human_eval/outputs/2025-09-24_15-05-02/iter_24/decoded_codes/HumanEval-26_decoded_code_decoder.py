from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: Counter[int] = Counter(list_of_numbers)
    result: List[int] = [number for number in list_of_numbers if counts[number] <= 1]
    return result