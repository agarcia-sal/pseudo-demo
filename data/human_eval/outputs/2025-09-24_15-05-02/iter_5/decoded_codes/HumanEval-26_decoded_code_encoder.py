from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    count_dictionary = Counter(numbers)
    result_list = []
    for number in numbers:
        if count_dictionary[number] <= 1:
            result_list.append(number)
    return result_list