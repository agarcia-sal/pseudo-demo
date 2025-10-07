from typing import List

def filter_by_prefix(sequence_of_words: List[str], initial_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    index_tracker: int = 0
    while not (index_tracker >= len(sequence_of_words)):
        current_element: str = sequence_of_words[index_tracker]
        if not (not current_element.startswith(initial_substring)):
            filtered_collection.append(current_element)
        index_tracker += 1
    return filtered_collection