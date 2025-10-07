from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    buffer_even: List[T] = []
    buffer_odd: List[T] = []

    for index in range(len(list_of_elements)):
        if index % 2 == 0:
            buffer_even.append(list_of_elements[index])
        else:
            buffer_odd.append(list_of_elements[index])

    buffer_even.sort()

    result: List[T] = []
    iter_ = 0
    limit = min(len(buffer_even), len(buffer_odd))
    while iter_ < limit:
        result.append(buffer_even[iter_])
        result.append(buffer_odd[iter_])
        iter_ += 1

    if len(buffer_even) > len(buffer_odd):
        result.append(buffer_even[-1])

    return result