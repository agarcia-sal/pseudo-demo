from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_counter = Counter(list_of_numbers)
    result_list = []
    for element in list_of_numbers:
        if frequency_counter[element] <= 1:
            result_list.append(element)
    return result_list