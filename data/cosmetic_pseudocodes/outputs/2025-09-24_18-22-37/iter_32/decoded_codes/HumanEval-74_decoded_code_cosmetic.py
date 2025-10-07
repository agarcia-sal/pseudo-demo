from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    accumulator_one: int = 0
    index_a: int = 0
    while index_a < len(list_one):
        current_element: str = list_one[index_a]
        partial_length: int = len(current_element)
        accumulator_one += partial_length
        index_a += 1

    accumulator_two: int = 0
    iterator_b: int = 0
    while iterator_b < len(list_two):
        element_b: str = list_two[iterator_b]
        length_b: int = len(element_b)
        accumulator_two += length_b
        iterator_b += 1

    if not (accumulator_one > accumulator_two):
        return list_one
    else:
        return list_two