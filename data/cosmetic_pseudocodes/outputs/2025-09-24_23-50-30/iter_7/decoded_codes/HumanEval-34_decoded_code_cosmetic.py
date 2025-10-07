from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_sequence: Iterable[T]) -> List[T]:
    temp_storage: List[T] = []
    seen_elements: dict[T, bool] = {}
    for element in input_sequence:
        if element not in seen_elements:
            seen_elements[element] = True
            temp_storage.append(element)

    sorted_output: List[T] = []
    index_counter: int = 0
    while index_counter < len(temp_storage):
        min_index = index_counter
        search_index = index_counter + 1
        while search_index < len(temp_storage):
            if temp_storage[search_index] < temp_storage[min_index]:
                min_index = search_index
            search_index += 1
        if min_index != index_counter:
            temp_storage[index_counter], temp_storage[min_index] = temp_storage[min_index], temp_storage[index_counter]
        index_counter += 1

    for value in temp_storage:
        sorted_output.append(value)

    return sorted_output