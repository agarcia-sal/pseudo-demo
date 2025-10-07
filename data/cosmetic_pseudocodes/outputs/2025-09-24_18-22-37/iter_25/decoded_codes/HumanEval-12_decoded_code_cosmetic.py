from typing import Optional, Sequence

def longest(collection_of_texts: Sequence[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    max_len_temp: int = 0
    idx_counter: int = 0
    while idx_counter < len(collection_of_texts):
        current_entry = collection_of_texts[idx_counter]
        current_length = 0
        char_index = 0
        while char_index < len(current_entry):
            current_length += 1
            char_index += 1
        if max_len_temp < current_length:
            max_len_temp = current_length
        idx_counter += 1

    loop_variable = 0
    while loop_variable < len(collection_of_texts):
        potential_candidate = collection_of_texts[loop_variable]
        candidate_length = 0
        position = 0
        while position < len(potential_candidate):
            candidate_length += 1
            position += 1
        if candidate_length == max_len_temp:
            return potential_candidate
        loop_variable += 1
    return None