from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_length_first: int = 0
    sum_length_second: int = 0

    index: int = 0
    while index < len(list_one):
        sum_length_first += len(list_one[index])
        index += 1

    index = 0
    while index < len(list_two):
        sum_length_second += len(list_two[index])
        index += 1

    if not (sum_length_first > sum_length_second):
        return list_one
    else:
        return list_two