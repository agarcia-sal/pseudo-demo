from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_even(sequence_param: Sequence[T]) -> List[T]:
    aggregate_result: List[T] = []

    temp_a: List[T] = []
    temp_b: List[T] = []

    counter_index = 0
    while counter_index < len(sequence_param):
        if counter_index % 2 == 0:
            temp_a.append(sequence_param[counter_index])
        else:
            temp_b.append(sequence_param[counter_index])
        counter_index += 1

    temp_a.sort()  # sort non-decreasing

    iterator_alpha = 0
    while iterator_alpha < len(temp_b):
        aggregate_result.append(temp_a[iterator_alpha])
        aggregate_result.append(temp_b[iterator_alpha])
        iterator_alpha += 1

    if len(temp_a) > len(temp_b):
        tail_value = temp_a[len(temp_a) - 1]
        aggregate_result.append(tail_value)

    return aggregate_result