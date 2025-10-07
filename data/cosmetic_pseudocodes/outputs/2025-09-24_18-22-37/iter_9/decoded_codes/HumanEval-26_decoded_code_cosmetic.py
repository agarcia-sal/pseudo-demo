from collections import Counter
from typing import List

def remove_duplicates(array_of_integers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(array_of_integers)
    result_sequence: List[int] = [item for item in array_of_integers if frequency_map[item] <= 1]
    return result_sequence