from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len = 0
    index_counter = 0

    while index_counter < len(list_of_strings):
        current_len = len(list_of_strings[index_counter])
        if current_len > max_len:
            max_len = current_len
        index_counter += 1

    def find_match(pos: int) -> Optional[str]:
        if pos == len(list_of_strings):
            return None
        if len(list_of_strings[pos]) == max_len:
            return list_of_strings[pos]
        return find_match(pos + 1)

    return find_match(0)