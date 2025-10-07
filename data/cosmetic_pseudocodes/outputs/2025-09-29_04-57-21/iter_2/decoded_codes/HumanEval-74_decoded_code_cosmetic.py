from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    sum_two: int = 0
    for index in range(len(list_one)):
        current_str: str = list_one[index]
        sum_one += len(current_str)
    loop_index: int = 0
    while loop_index < len(list_two):
        element: str = list_two[loop_index]
        sum_two += len(element)
        loop_index += 1
    if not (sum_one > sum_two):
        return list_one
    return list_two