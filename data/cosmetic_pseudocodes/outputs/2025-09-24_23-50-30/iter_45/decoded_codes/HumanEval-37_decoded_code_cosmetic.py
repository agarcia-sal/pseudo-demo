from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    array_a: List[T] = []
    array_b: List[T] = []
    index_i: int = 0

    while index_i < len(list_of_elements):
        if index_i % 2 == 0:
            array_a.append(list_of_elements[index_i])
        else:
            array_b.append(list_of_elements[index_i])
        index_i += 1

    array_a.sort()

    result_container: List[T] = []
    iter_j: int = 0

    while iter_j < len(array_b):
        result_container.append(array_a[iter_j])
        result_container.append(array_b[iter_j])
        iter_j += 1

    if len(array_a) - len(array_b) > 0:
        result_container.append(array_a[-1])

    return result_container