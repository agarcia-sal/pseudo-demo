from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counter = Counter(list_of_numbers)
    return [element for element in list_of_numbers if counter[element] <= 1]