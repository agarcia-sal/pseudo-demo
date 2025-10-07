from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_chars_first: int = 0
    index_first: int = 0
    while index_first < len(list_one):
        sum_chars_first += len(list_one[index_first])
        index_first += 1

    sum_chars_second: int = 0
    index_second: int = 0
    while index_second < len(list_two):
        sum_chars_second += len(list_two[index_second])
        index_second += 1

    if not (sum_chars_first > sum_chars_second):
        return list_one
    else:
        return list_two