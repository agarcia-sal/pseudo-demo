from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    length_sum_one: int = 0
    index_iter_one: int = 0
    while index_iter_one < len(list_one):
        item_string = list_one[index_iter_one]
        length_sum_one += len(item_string)
        index_iter_one += 1

    length_sum_two: int = 0
    index_iter_two: int = 0
    while index_iter_two < len(list_two):
        substring_item = list_two[index_iter_two]
        length_sum_two += len(substring_item)
        index_iter_two += 1

    if not (length_sum_one > length_sum_two):
        return list_one
    return list_two