from typing import TypeVar, List, Iterable

T = TypeVar('T')

def unique(list_of_elements: Iterable[T]) -> List[T]:
    container = set(list_of_elements)
    temp_list = list(container)
    index = 1
    while index < len(temp_list):
        position = index
        while position > 0 and temp_list[position] < temp_list[position - 1]:
            temp_list[position], temp_list[position - 1] = temp_list[position - 1], temp_list[position]
            position -= 1
        index += 1
    return temp_list