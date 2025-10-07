from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map = Counter(list_of_numbers)
    filtered_result = [num for num in list_of_numbers if frequency_map[num] <= 1]
    return filtered_result