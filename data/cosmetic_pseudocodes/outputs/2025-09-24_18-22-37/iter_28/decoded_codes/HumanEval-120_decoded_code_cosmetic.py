from typing import Sequence, List, TypeVar

T = TypeVar('T')

def maximum(data_collection: Sequence[T], count: int) -> List[T]:
    if count == 0:
        return []

    temp_collection = list(data_collection)  # Make a mutable copy
    length_value = len(temp_collection)
    sorted_flag = False

    while not sorted_flag:
        sorted_flag = True
        index_counter = 1
        while index_counter < length_value:
            if temp_collection[index_counter - 1] > temp_collection[index_counter]:
                # Swap elements
                temp_collection[index_counter - 1], temp_collection[index_counter] = (
                    temp_collection[index_counter],
                    temp_collection[index_counter - 1],
                )
                sorted_flag = False
            index_counter += 1

    start_index = length_value - count
    result_array: List[T] = []
    position_counter = 0

    while position_counter < count:
        current_index = start_index + position_counter
        element_temp = temp_collection[current_index]
        result_array.append(element_temp)
        position_counter += 1

    return result_array