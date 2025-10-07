from typing import List

def filter_by_prefix(array_of_texts: List[str], edge_text: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(array_of_texts):
        candidate_string: str = array_of_texts[iterator_index]
        if candidate_string.startswith(edge_text):
            filtered_collection.append(candidate_string)
        iterator_index += 1
    return filtered_collection