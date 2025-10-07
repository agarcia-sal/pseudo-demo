from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_sorted_list: List[int] = []
    seen_elements: List[int] = []
    for index in range(len(lst)):
        current_element = lst[index]
        element_already_seen = False
        for seen_index in range(len(seen_elements)):
            if seen_elements[seen_index] == current_element:
                element_already_seen = True
                break
        if not element_already_seen:
            seen_elements.append(current_element)
    while len(seen_elements) > 0:
        min_element = seen_elements[0]
        min_index = 0
        for element_index in range(1, len(seen_elements)):
            if seen_elements[element_index] < min_element:
                min_element = seen_elements[element_index]
                min_index = element_index
        unique_sorted_list.append(min_element)
        seen_elements.pop(min_index)
    if len(unique_sorted_list) < 2:
        return None
    else:
        return unique_sorted_list[1]