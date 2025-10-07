from typing import List, Optional

def longest(input_strings: List[str]) -> Optional[str]:
    if len(input_strings) == 0:
        return None

    max_len: int = 0
    i: int = 0
    while i < len(input_strings):
        if len(input_strings[i]) > max_len:
            max_len = len(input_strings[i])
        i += 1

    j: int = 0
    while j < len(input_strings):
        if len(input_strings[j]) == max_len:
            return input_strings[j]
        j += 1

    return None  # In theory unreachable