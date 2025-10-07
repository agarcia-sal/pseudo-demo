from typing import List, Union, Sequence


def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    sum_length_one: int = 0
    iterator_one: int = 0
    while iterator_one < len(list_one):
        current_item: str = list_one[iterator_one]
        sum_length_one += len(current_item)
        iterator_one += 1

    sum_length_two: int = 0
    index_two: int = 0
    while index_two < len(list_two):
        elem: str = list_two[index_two]
        sum_length_two += len(elem)
        index_two += 1

    return list_one if sum_length_one <= sum_length_two else list_two