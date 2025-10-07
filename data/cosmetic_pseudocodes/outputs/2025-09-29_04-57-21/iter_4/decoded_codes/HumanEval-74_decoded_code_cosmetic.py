from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_lengths_one: int = 0
    iterator_one: int = 0
    while iterator_one < len(list_one):
        current_string: str = list_one[iterator_one]
        sum_lengths_one += len(current_string)
        iterator_one += 1

    sum_lengths_two: int = 0
    iterator_two: int = 0
    while iterator_two < len(list_two):
        current_string_two: str = list_two[iterator_two]
        sum_lengths_two += len(current_string_two)
        iterator_two += 1

    if not (sum_lengths_one > sum_lengths_two):
        return list_one
    else:
        return list_two