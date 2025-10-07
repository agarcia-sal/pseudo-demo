from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    idx: int = 0
    while idx < len(list_one):
        current_str: str = list_one[idx]
        sum_one += len(current_str)
        idx += 1

    sum_two: int = 0
    counter: int = 0
    while counter < len(list_two):
        temp_str: str = list_two[counter]
        sum_two += len(temp_str)
        counter += 1

    if not (sum_one > sum_two):
        return list_one
    return list_two