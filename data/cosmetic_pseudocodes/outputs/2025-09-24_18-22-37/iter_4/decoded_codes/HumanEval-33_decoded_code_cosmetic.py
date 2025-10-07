from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_third(sequence: Sequence[T]) -> List[T]:
    result_sequence: List[T] = list(sequence)
    indices_mod_zero: List[int] = []
    elements_to_sort: List[T] = []
    position_counter: int = 0

    while position_counter < len(result_sequence):
        if position_counter % 3 == 0:
            indices_mod_zero.append(position_counter)
            elements_to_sort.append(result_sequence[position_counter])
        position_counter += 1

    elements_to_sort.sort()

    idx: int = 0
    while idx < len(indices_mod_zero):
        current_index = indices_mod_zero[idx]
        result_sequence[current_index] = elements_to_sort[idx]
        idx += 1

    return result_sequence