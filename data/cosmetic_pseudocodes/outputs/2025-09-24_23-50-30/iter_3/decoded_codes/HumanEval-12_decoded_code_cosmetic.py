from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None
    max_len: int = 0
    for i in range(len(list_of_strings)):
        current_len = len(list_of_strings[i])
        if current_len > max_len:
            max_len = current_len
    for j in range(len(list_of_strings)):
        if len(list_of_strings[j]) == max_len:
            return list_of_strings[j]