from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_slice: List[T] = []
    second_slice: List[T] = []
    for step_index in range(len(list_of_elements)):
        if step_index % 2 == 0:
            first_slice.append(list_of_elements[step_index])
        else:
            second_slice.append(list_of_elements[step_index])
    result_sequence: List[T] = []
    put_sorted_into(first_slice, second_slice, result_sequence)
    return result_sequence

def put_sorted_into(arr_one: List[T], arr_two: List[T], accumulator: List[T]) -> None:
    if len(arr_one) > len(arr_two):
        arr_two.sort()
        arr_one.sort()
    else:
        arr_one.sort()
        arr_two.sort()
    current_pos = 0
    limit = min(len(arr_one), len(arr_two))
    while current_pos < limit:
        accumulator.extend([arr_one[current_pos], arr_two[current_pos]])
        current_pos += 1
    if len(arr_one) > len(arr_two):
        accumulator.append(arr_one[-1])