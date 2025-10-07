from collections import Counter
from typing import List

def remove_duplicates(list_of_integers: List[int]) -> List[int]:
    element_counts = Counter(list_of_integers)
    return [element for element in list_of_integers if element_counts[element] <= 1]