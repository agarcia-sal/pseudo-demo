from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts = Counter(list_of_numbers)
    return [number for number in list_of_numbers if counts[number] <= 1]