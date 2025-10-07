from typing import Optional, Sequence


def longest(collection_of_strings: Sequence[str]) -> Optional[str]:
    if not collection_of_strings:
        return None

    temp_max_length: int = 0
    temp_index: int = 0
    while temp_index < len(collection_of_strings):
        current_element: str = collection_of_strings[temp_index]
        current_length: int = len(current_element)
        if current_length > temp_max_length:
            temp_max_length = current_length
        temp_index += 1

    iterator_position: int = 0
    while iterator_position < len(collection_of_strings):
        candidate_string: str = collection_of_strings[iterator_position]
        candidate_length: int = len(candidate_string)
        if candidate_length == temp_max_length:
            return candidate_string
        iterator_position += 1

    return None  # fallback, though logically unreachable