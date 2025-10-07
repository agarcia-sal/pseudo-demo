from typing import Optional, List

def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    highest_size: int = float('-inf')
    index_counter: int = 0
    while index_counter < len(array_of_texts):
        current_text = array_of_texts[index_counter]
        if len(current_text) > highest_size:
            highest_size = len(current_text)
        index_counter += 1

    position: int = 0
    while position < len(array_of_texts):
        if len(array_of_texts[position]) == highest_size:
            return array_of_texts[position]
        position += 1

    return None  # fallback, should not be reached