from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_length_a: int = 0
    index_a: int = 0
    while index_a < len(list_one):
        sum_length_a += len(list_one[index_a])
        index_a += 1

    sum_length_b: int = 0
    index_b: int = 0
    while index_b < len(list_two):
        sum_length_b += len(list_two[index_b])
        index_b += 1

    if sum_length_a > sum_length_b:
        return list_two
    else:
        return list_one