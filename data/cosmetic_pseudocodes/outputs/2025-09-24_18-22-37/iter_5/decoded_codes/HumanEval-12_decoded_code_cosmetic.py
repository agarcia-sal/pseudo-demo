from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    longest_size = 0
    for current_text in array_of_texts:
        current_length = len(current_text)
        if current_length > longest_size:
            longest_size = current_length

    position = 0
    while position < len(array_of_texts):
        candidate_text = array_of_texts[position]
        if len(candidate_text) == longest_size:
            return candidate_text
        position += 1

    return None  # Just in case, although logically unreachable