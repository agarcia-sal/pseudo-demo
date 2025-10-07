from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    accumulated_a: int = 0
    iterator_x: int = 0
    while iterator_x < len(list_one):
        temp_var1: T = list_one[iterator_x]
        length_var: int = len(temp_var1)
        accumulated_a += length_var
        iterator_x += 1

    accumulated_b: int = 0
    iterator_y: int = 0
    while iterator_y < len(list_two):
        temp_var2: T = list_two[iterator_y]
        length_var2: int = len(temp_var2)
        accumulated_b += length_var2
        iterator_y += 1

    if accumulated_a <= accumulated_b:
        result_ref: List[T] = list_one
    else:
        result_ref = list_two

    return result_ref