from typing import List

def filter_by_prefix(sequence_of_texts: List[str], initial_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    index_tracker: int = 0
    length_tracker: int = len(sequence_of_texts)

    while index_tracker < length_tracker:
        current_element: str = sequence_of_texts[index_tracker]
        if current_element.startswith(initial_substring):
            filtered_collection.append(current_element)
        index_tracker += 1

    return filtered_collection