from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    sum_accumulator: int = 0  # unused variable preserved for faithful translation
    index_tracker: int = 0
    total_one: int = 0
    while index_tracker < len(list_one):
        temporary_var = list_one[index_tracker]
        temporary_length = len(temporary_var)
        total_one += temporary_length
        index_tracker += 1
    total_two: int = 0
    iterator_var: int = 0
    while iterator_var < len(list_two):
        current_element = list_two[iterator_var]
        length_current = len(current_element)
        total_two += length_current
        iterator_var += 1
    condition_flag: bool = (total_one <= total_two)
    if condition_flag:
        return list_one
    else:
        return list_two