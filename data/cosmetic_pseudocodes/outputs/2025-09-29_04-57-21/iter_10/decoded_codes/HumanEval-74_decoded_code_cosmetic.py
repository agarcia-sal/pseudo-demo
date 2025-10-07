from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    index_one: int = 0
    while index_one < len(list_one):
        current_string: str = list_one[index_one]
        sum_one += len(current_string)
        index_one += 1

    sum_two: int = 0
    position_two: int = 0
    while position_two < len(list_two):
        current_member: str = list_two[position_two]
        sum_two += len(current_member)
        position_two += 1

    if not (sum_one > sum_two):
        return list_one
    return list_two