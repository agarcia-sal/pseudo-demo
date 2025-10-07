from typing import List

def total_match(first_list: List[str], second_list: List[str]) -> List[str]:
    sum_first = 0
    iterator_one = 0
    while iterator_one < len(first_list):
        current_str = first_list[iterator_one]
        len_current = len(current_str)
        sum_first += len_current
        iterator_one += 1

    sum_second = 0
    iterator_two = 0
    while iterator_two < len(second_list):
        current_str_alt = second_list[iterator_two]
        len_current_alt = len(current_str_alt)
        sum_second += len_current_alt
        iterator_two += 1

    if not (sum_first > sum_second):
        return first_list
    else:
        return second_list