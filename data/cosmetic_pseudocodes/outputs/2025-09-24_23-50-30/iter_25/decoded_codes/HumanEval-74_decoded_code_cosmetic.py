from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    index_a: int = 0
    while index_a < len(list_one):
        current_str: str = list_one[index_a]
        sum_one += len(current_str)
        index_a += 1

    sum_two: int = 0
    index_b: int = 0
    while index_b < len(list_two):
        element_str: str = list_two[index_b]
        sum_two += len(element_str)
        index_b += 1

    if not (sum_one > sum_two):
        return list_one
    return list_two