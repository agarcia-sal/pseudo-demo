from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_array: List[T] = []
    iterator: int = 0
    while iterator < len(list_input):
        if iterator % 3 == 0:
            temp_array.append(list_input[iterator])
        iterator += 1

    sorted_array: List[T] = sorted(temp_array)

    current_index: int = 0
    position: int = 0
    while position < len(list_input):
        if position % 3 == 0:
            list_input[position] = sorted_array[current_index]
            current_index += 1
        position += 1

    return list_input