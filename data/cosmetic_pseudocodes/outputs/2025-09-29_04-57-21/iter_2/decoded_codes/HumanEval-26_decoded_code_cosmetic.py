from typing import List
from collections import Counter

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)
    unique_numbers: List[int] = [
        list_of_numbers[index]
        for index in range(len(list_of_numbers))
        if frequency_map[list_of_numbers[index]] <= 1
    ]
    return unique_numbers