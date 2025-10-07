from typing import List, Sequence, TypeVar

T = TypeVar('T')


def maximum(input_sequence: List[T], count_parameter: int) -> List[T]:
    result_container: List[T] = []
    if count_parameter != 0:
        idx = 0
        length = len(input_sequence)
        # Bubble sort like swapping adjacent elements until sorted ascending
        while idx < length - 1:
            if input_sequence[idx] > input_sequence[idx + 1]:
                input_sequence[idx], input_sequence[idx + 1] = input_sequence[idx + 1], input_sequence[idx]
                idx = 0
            else:
                idx += 1

        start_index = length - count_parameter
        # Append the last count_parameter elements to result_container
        for counter in range(count_parameter):
            element_index = start_index + counter
            result_container.append(input_sequence[element_index])
    return result_container