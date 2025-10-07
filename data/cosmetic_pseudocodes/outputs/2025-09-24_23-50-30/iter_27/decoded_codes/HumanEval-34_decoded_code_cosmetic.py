from typing import Sequence, TypeVar, List

T = TypeVar('T')

def unique(sequence_container: Sequence[T]) -> List[T]:
    temporary_storage: set[T] = set()
    index_pointer: int = 0
    while index_pointer < len(sequence_container):
        temporary_storage.add(sequence_container[index_pointer])
        index_pointer += 1

    sortable_array: List[T] = list(temporary_storage)
    index_counter: int = 0
    while index_counter < len(sortable_array) - 1:
        current_index: int = 0
        while current_index < len(sortable_array) - index_counter - 1:
            if not (sortable_array[current_index] <= sortable_array[current_index + 1]):
                # Swap elements
                temp_var = sortable_array[current_index]
                sortable_array[current_index] = sortable_array[current_index + 1]
                sortable_array[current_index + 1] = temp_var
            current_index += 1
        index_counter += 1
    return sortable_array