from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def search(index: int, max_len: int) -> Optional[str]:
        if index == len(list_of_strings):
            return None
        candidate = list_of_strings[index]
        if len(candidate) == max_len:
            return candidate
        return search(index + 1, max_len)

    if not list_of_strings:
        return None

    lengths: List[int] = []
    position = 0
    while position < len(list_of_strings):
        lengths.append(len(list_of_strings[position]))
        position += 1

    max_length = lengths[0]
    idx = 1
    while idx < len(lengths):
        if max_length < lengths[idx]:
            max_length = lengths[idx]
        idx += 1

    return search(0, max_length)