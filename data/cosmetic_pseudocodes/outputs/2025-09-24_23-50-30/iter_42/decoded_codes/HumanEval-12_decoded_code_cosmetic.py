from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    def helper(idx: int, max_len: int) -> Optional[str]:
        if idx >= len(list_of_strings):
            return None
        if len(list_of_strings[idx]) == max_len:
            return list_of_strings[idx]
        else:
            return helper(idx + 1, max_len)

    if not list_of_strings:
        return None

    longest_length = 0
    temp_index = 0
    while temp_index < len(list_of_strings):
        if len(list_of_strings[temp_index]) > longest_length:
            longest_length = len(list_of_strings[temp_index])
        temp_index += 1

    return helper(0, longest_length)