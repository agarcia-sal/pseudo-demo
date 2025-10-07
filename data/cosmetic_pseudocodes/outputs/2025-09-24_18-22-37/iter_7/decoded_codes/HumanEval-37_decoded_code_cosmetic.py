from typing import Sequence, List, TypeVar

T = TypeVar('T')


def sort_even(input_sequence: Sequence[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    position_counter: int = 0

    while position_counter < len(input_sequence):
        if position_counter % 2 == 0:
            first_subset.append(input_sequence[position_counter])
        else:
            second_subset.append(input_sequence[position_counter])
        position_counter += 1

    first_subset.sort()

    output_sequence: List[T] = []
    idx: int = 0
    min_length: int = len(second_subset)

    while idx < min_length:
        output_sequence.append(first_subset[idx])
        output_sequence.append(second_subset[idx])
        idx += 1

    if len(first_subset) > len(second_subset):
        output_sequence.append(first_subset[-1])

    return output_sequence