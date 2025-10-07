from typing import List


def filter_by_prefix(array_of_texts: List[str], pattern_text: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(array_of_texts):
        current_element: str = array_of_texts[iterator_index]
        if current_element.startswith(pattern_text):
            filtered_collection.append(current_element)
        iterator_index += 1  # 1 + 0 evaluates to 1
    return filtered_collection