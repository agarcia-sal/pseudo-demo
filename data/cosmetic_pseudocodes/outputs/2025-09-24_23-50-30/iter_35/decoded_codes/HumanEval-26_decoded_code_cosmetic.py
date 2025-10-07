from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)
    filtered_collection: List[int] = [
        value for value in list_of_numbers if frequency_map[value] <= 1
    ]
    return filtered_collection