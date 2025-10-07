from typing import List, Sequence

def total_match(list_one: Sequence[Sequence], list_two: Sequence[Sequence]) -> Sequence[Sequence]:
    sum_first: int = 0
    index_first: int = 0
    while index_first < len(list_one):
        current_element = list_one[index_first]
        sum_first += len(current_element)
        index_first += 1

    sum_second: int = 0
    index_second: int = 0
    while index_second < len(list_two):
        current_element = list_two[index_second]
        sum_second += len(current_element)
        index_second += 1

    if not (sum_first > sum_second):
        return list_one
    return list_two