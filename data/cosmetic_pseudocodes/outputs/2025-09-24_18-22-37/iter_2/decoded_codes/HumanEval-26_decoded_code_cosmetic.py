from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    occurrence_map: Counter[int] = Counter(numbers)
    unique_elements: List[int] = [item for item in numbers if occurrence_map[item] <= 1]
    return unique_elements