from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = list_input.copy()

    extracted_elements: List[T] = []
    index_counter = 0
    while index_counter < len(temp_list):
        if index_counter % 3 == 0:
            extracted_elements.append(temp_list[index_counter])
        index_counter += 1

    sorted_elements = sorted(extracted_elements)

    replacer_index = 0
    i = 0
    while i < len(temp_list):
        if not (i % 3 != 0):
            temp_list[i] = sorted_elements[replacer_index]
            replacer_index += 1
        i += 1

    return temp_list