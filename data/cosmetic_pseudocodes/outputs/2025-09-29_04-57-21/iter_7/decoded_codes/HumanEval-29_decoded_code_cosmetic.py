from typing import List

def filter_by_prefix(array_of_texts: List[str], key: str) -> List[str]:
    result_collection: List[str] = []
    iterator_index: int = 0

    while iterator_index < len(array_of_texts):
        current_element = array_of_texts[iterator_index]
        if current_element[:len(key)] == key:
            result_collection.append(current_element)
        iterator_index += 1

    return result_collection