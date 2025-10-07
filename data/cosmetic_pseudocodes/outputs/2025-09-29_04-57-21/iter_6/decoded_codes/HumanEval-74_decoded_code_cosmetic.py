from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_chars_first: int = 0
    idx_first: int = 0
    while idx_first < len(list_one):
        current_str: str = list_one[idx_first]
        sum_chars_first += len(current_str)
        idx_first += 1

    sum_chars_second: int = 0
    iterator_second: int = 0
    while iterator_second < len(list_two):
        element_str: str = list_two[iterator_second]
        sum_chars_second += len(element_str)
        iterator_second += 1

    if not (sum_chars_first > sum_chars_second):
        return list_one
    else:
        return list_two