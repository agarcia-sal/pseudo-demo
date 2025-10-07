from bisect import insort
from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_list: List[int] = []
    for element in array_of_integers:
        insort(sorted_list, element)
    result_list: List[int] = []
    index: int = len(sorted_list)
    while positive_integer_k > 0 and index > 0:
        index -= 1
        result_list.insert(0, sorted_list[index])  # add to front
        positive_integer_k -= 1
    return result_list