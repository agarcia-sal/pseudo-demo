from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    element_counts: Counter[int] = Counter(list_of_numbers)
    result_list: List[int] = [num for num in list_of_numbers if element_counts[num] <= 1]
    return result_list