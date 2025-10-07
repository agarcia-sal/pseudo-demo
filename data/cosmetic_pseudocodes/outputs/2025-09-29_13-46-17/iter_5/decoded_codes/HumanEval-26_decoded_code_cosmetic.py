from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    count_map: Counter[int] = Counter(list_of_numbers)
    filtered_list: List[int] = [
        num for num in list_of_numbers if count_map[num] == 1
    ]
    return filtered_list