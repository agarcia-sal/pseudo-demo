from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    count_map: Counter[int] = Counter(list_of_numbers)
    result_list: List[int] = []
    for number in list_of_numbers:
        if count_map[number] <= 1:
            result_list.append(number)
    return result_list