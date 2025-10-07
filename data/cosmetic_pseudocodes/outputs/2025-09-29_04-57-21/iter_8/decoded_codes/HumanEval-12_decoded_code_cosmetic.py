from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = -1
    iterator: int = 0
    while iterator < len(list_of_strings):
        length = len(list_of_strings[iterator])
        if length > max_len:
            max_len = length
        iterator += 1

    cursor: int = 0
    while cursor < len(list_of_strings):
        if len(list_of_strings[cursor]) == max_len:
            return list_of_strings[cursor]
        cursor += 1