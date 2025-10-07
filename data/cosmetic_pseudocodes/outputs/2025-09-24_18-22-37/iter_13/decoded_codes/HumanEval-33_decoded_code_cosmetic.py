from typing import List, TypeVar

T = TypeVar('T')


def sort_third(array_param: List[T]) -> List[T]:
    local_array: List[T] = array_param[:]  # duplicate the list
    indices_collection: List[int] = []
    collected_elements: List[T] = []

    iterator_index = 0
    while iterator_index < len(local_array):
        if iterator_index % 3 == 0:
            indices_collection.append(iterator_index)
            collected_elements.append(local_array[iterator_index])
        iterator_index += 1

    ascending_sorted = sorted(collected_elements)

    position = 0
    while True:
        if position >= len(indices_collection):
            break
        local_array[indices_collection[position]] = ascending_sorted[position]
        position += 1

    return local_array