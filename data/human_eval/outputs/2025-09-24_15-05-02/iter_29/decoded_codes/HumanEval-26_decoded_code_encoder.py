from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    element_counts = Counter(list_of_numbers)
    result_list = [element for element in list_of_numbers if element_counts[element] <= 1]
    return result_list