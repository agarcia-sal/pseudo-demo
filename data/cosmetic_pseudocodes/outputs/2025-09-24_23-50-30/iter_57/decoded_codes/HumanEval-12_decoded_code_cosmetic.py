from typing import Collection, Optional

def longest(collection_of_words: Collection[str]) -> Optional[str]:
    # tail_loop
    while len(collection_of_words) != 0:
        max_len_var: int = 0
        index_var: int = 0  # unused in logic, but preserved
        temp_index: int = 0
        while temp_index < len(collection_of_words):
            if max_len_var < len(collection_of_words[temp_index]):
                max_len_var = len(collection_of_words[temp_index])
            temp_index += 1

        position_counter: int = 0
        found_result: Optional[str] = None
        while True:
            if position_counter >= len(collection_of_words) or found_result is not None:
                break
            if len(collection_of_words[position_counter]) == max_len_var:
                found_result = collection_of_words[position_counter]
                return found_result
            position_counter += 1
        break  # exit tail_loop after first iteration
    return None