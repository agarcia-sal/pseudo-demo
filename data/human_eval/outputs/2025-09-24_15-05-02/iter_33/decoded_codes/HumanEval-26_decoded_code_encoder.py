from collections import Counter
from typing import List

def remove_duplicates(list_of_integers: List[int]) -> List[int]:
    count_dictionary: Counter[int] = Counter(list_of_integers)
    result_list: List[int] = [integer for integer in list_of_integers if count_dictionary[integer] <= 1]
    return result_list