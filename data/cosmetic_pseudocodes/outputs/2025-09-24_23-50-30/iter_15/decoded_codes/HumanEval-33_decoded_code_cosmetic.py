from collections import deque
from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    copy_of_list: deque[T] = deque()
    for index in range(len(list_input)):
        copy_of_list.append(list_input[index])

    extracted_elements: List[T] = []
    position = 0
    while position < len(copy_of_list):
        if position % 3 == 0:
            extracted_elements.append(copy_of_list[position])
        position += 1

    ordered_elements: List[T] = []
    while extracted_elements:
        minimum_element = extracted_elements[0]
        min_index = 0
        for search_index in range(1, len(extracted_elements)):
            if extracted_elements[search_index] < minimum_element:
                minimum_element = extracted_elements[search_index]
                min_index = search_index
        ordered_elements.append(minimum_element)
        extracted_elements.pop(min_index)

    insert_pos = 0
    for idx in range(len(copy_of_list)):
        if idx % 3 == 0:
            copy_of_list[idx] = ordered_elements[insert_pos]
            insert_pos += 1

    return list(copy_of_list)