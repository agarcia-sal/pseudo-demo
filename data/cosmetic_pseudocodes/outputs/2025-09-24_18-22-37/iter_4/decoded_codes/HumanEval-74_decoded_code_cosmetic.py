from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_length_one: int = 0
    index_one: int = 0
    while index_one < len(list_one):
        current_str_one: str = list_one[index_one]
        sum_length_one += len(current_str_one)
        index_one += 1

    sum_length_two: int = 0
    counter_two: int = 0
    while counter_two < len(list_two):
        current_str_two: str = list_two[counter_two]
        sum_length_two += len(current_str_two)
        counter_two += 1

    if sum_length_one <= sum_length_two:
        return list_one
    else:
        return list_two