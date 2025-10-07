from typing import List

def filter_by_prefix(container_list: List[str], head_string: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(container_list):
        current_element = container_list[iterator_index]
        if current_element[:len(head_string)] == head_string:
            filtered_collection.append(current_element)
        iterator_index += 1
    return filtered_collection