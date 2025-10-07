from typing import List

def filter_by_prefix(collection_of_strings: List[str], initial_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    current_index: int = 0
    total_elements: int = len(collection_of_strings)

    while current_index < total_elements:
        candidate_element: str = collection_of_strings[current_index]
        length_of_prefix: int = len(initial_substring)
        substring_candidate: str = candidate_element[:length_of_prefix]

        if substring_candidate == initial_substring:
            filtered_collection.append(candidate_element)

        current_index += 1

    return filtered_collection