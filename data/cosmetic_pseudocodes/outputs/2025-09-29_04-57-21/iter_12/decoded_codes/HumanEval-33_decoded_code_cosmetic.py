from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    cloned_list: List[T] = list_input[:]  # clone the input list
    temp_collection: List[T] = []
    index_counter: int = 0

    while index_counter < len(cloned_list):
        if index_counter % 3 == 0:
            temp_collection.append(cloned_list[index_counter])
        index_counter += 1

    temp_collection.sort()

    replacement_index: int = 0
    index_counter = 0

    while index_counter < len(cloned_list):
        if index_counter % 3 == 0:
            cloned_list[index_counter] = temp_collection[replacement_index]
            replacement_index += 1
        index_counter += 1

    return cloned_list