from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    accumulator_a: int = 0
    iterator_b: int = 0
    while iterator_b < len(list_one):
        current_element_c: T = list_one[iterator_b]
        temp_length_d: int = len(current_element_c)
        accumulator_a += temp_length_d
        iterator_b += 1

    accumulator_e: int = 0
    iterator_f: int = 0
    while iterator_f < len(list_two):
        current_element_g: T = list_two[iterator_f]
        temp_length_h: int = len(current_element_g)
        accumulator_e += temp_length_h
        iterator_f += 1

    flag_result: bool = False
    if accumulator_a <= accumulator_e:
        flag_result = True

    if flag_result:
        return list_one
    else:
        return list_two