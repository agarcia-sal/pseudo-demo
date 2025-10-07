from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    elements_accumulated: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_of_elements):
        temp_element: int = list_of_elements[index_counter]
        elements_accumulated.append(1 + temp_element)
        index_counter += 1
    return elements_accumulated