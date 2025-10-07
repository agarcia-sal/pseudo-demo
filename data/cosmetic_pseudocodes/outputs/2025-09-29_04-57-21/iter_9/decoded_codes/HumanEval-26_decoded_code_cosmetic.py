from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)
    result_list: List[int] = [number for number in list_of_numbers if frequency_map[number] == 1]
    return result_list