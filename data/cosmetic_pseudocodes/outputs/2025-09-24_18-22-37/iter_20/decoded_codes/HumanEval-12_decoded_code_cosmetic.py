from typing import Optional, Sequence


def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    current_index: int = 0
    longest_length_found: int = 0
    total_elements: int = 0

    # Count total elements manually as per pseudocode
    while total_elements < len(collection_of_texts):
        total_elements += 1

    if total_elements == 0:
        return None

    # Find the longest length found
    current_index = 0
    while current_index < total_elements:
        element_at_index = collection_of_texts[current_index]
        current_length = len(element_at_index)
        if current_length > longest_length_found:
            longest_length_found = current_length
        current_index += 1

    # Return the first element with the longest length
    current_index = 0
    while current_index < total_elements:
        element_at_index = collection_of_texts[current_index]
        current_length = len(element_at_index)
        if current_length == longest_length_found:
            return element_at_index
        current_index += 1

    return None  # fallback, though logically unreachable