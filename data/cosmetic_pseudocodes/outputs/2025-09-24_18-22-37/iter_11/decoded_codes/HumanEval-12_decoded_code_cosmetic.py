from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len_temp: int = 0
    idx_counter: int = 0
    while idx_counter < len(list_of_strings):
        current_str: str = list_of_strings[idx_counter]
        current_len: int = len(current_str)
        if current_len > max_len_temp:
            max_len_temp = current_len
        idx_counter += 1

    search_index: int = 0
    while search_index < len(list_of_strings):
        candidate_str: str = list_of_strings[search_index]
        candidate_len: int = len(candidate_str)
        if candidate_len == max_len_temp:
            return candidate_str
        search_index += 1
    return None