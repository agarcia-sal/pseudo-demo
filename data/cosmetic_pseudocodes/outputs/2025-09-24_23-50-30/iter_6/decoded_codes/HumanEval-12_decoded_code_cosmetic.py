from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not (list_of_strings != []):
        return None

    lengths: List[int] = []
    index = 0
    while index < len(list_of_strings):
        lengths.append(len(list_of_strings[index]))
        index += 1

    max_len = -1
    scan = 0
    while scan < len(lengths):
        if lengths[scan] > max_len:
            max_len = lengths[scan]
        scan += 1

    pos = 0
    while pos < len(list_of_strings):
        if (len(list_of_strings[pos]) - max_len) % max_len == 0:
            return list_of_strings[pos]
        pos += 1

    return None