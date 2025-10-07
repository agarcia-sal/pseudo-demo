from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    accumulated_length_first: int = 0
    index_first: int = 0
    while index_first < len(list_one):
        current_string: str = list_one[index_first]
        length_current: int = len(current_string)
        accumulated_length_first += length_current
        index_first += 1

    accumulated_length_second: int = 0
    index_second: int = 0
    while index_second < len(list_two):
        current_candidate: str = list_two[index_second]
        length_candidate: int = len(current_candidate)
        accumulated_length_second += length_candidate
        index_second += 1

    if accumulated_length_first <= accumulated_length_second:
        return list_one
    else:
        return list_two