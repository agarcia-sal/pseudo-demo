from typing import List

def filter_by_prefix(sequence_of_texts: List[str], initial_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0

    while iterator_index < len(sequence_of_texts):
        current_element: str = sequence_of_texts[iterator_index]

        if current_element[:len(initial_substring)] == initial_substring:
            filtered_collection.append(current_element)

        iterator_index += 1

    return filtered_collection