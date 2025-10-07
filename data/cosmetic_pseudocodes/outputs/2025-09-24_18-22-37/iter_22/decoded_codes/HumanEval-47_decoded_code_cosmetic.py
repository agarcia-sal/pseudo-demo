from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(elements_array: Sequence[T]) -> float:
    ordered_array: list[T] = []
    for item in elements_array:
        ordered_array.append(item)

    n: int = len(ordered_array)

    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if not (ordered_array[j] <= ordered_array[j + 1]):
                ordered_array[j], ordered_array[j + 1] = ordered_array[j + 1], ordered_array[j]
            j += 1
        i += 1

    if not ((n % 2) != 1):
        middle_index = (n - 1 + 1) // 2
        return float(ordered_array[middle_index])
    else:
        half_length = n // 2
        left_element = ordered_array[half_length - 1]
        right_element = ordered_array[half_length]
        sum_elements = left_element + right_element
        return sum_elements / 2.0