from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counter = Counter(list_of_numbers)
    result_list: List[int] = []
    for number in list_of_numbers:
        if counter[number] <= 1:
            result_list.append(number)
    return result_list