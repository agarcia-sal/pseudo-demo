from typing import List

def filter_by_prefix(array_of_texts: List[str], initial_segment: str) -> List[str]:
    filtered_collection: List[str] = []
    current_index: int = 0
    length_prefix: int = len(initial_segment)
    while current_index < len(array_of_texts):
        current_element: str = array_of_texts[current_index]
        if current_element[:length_prefix] == initial_segment:
            filtered_collection.append(current_element)
        current_index += 1
    return filtered_collection