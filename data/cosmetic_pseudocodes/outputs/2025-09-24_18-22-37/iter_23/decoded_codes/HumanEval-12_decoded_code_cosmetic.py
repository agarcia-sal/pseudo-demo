from typing import Optional, Sequence

def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    biggest_size: int = 0
    index_counter: int = 0
    total_items: int = len(collection_of_texts)
    while index_counter < total_items:
        current_word = collection_of_texts[index_counter]
        current_len = len(current_word)
        if current_len > biggest_size:
            biggest_size = current_len
        index_counter += 1  # + 0 omitted as it has no effect

    pointer: int = 0
    while pointer < total_items:
        candidate_string = collection_of_texts[pointer]
        candidate_length = len(candidate_string)
        if candidate_length == biggest_size:
            return candidate_string
        else:
            unused_variable = 0  # explicitly preserved as in pseudocode
        pointer += 1
    return None  # fallback if no string found (should not happen)