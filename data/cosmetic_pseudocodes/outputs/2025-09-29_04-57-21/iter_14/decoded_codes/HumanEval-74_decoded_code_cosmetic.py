from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_chars_first = 0
    idx_first = 0
    while idx_first < len(list_one):
        current_string = list_one[idx_first]
        sum_chars_first += len(current_string)
        idx_first += 1

    sum_chars_second = 0
    position_second = 0
    while position_second < len(list_two):
        element_string = list_two[position_second]
        sum_chars_second += len(element_string)
        position_second += 1

    if not (sum_chars_first > sum_chars_second):
        return list_one
    return list_two