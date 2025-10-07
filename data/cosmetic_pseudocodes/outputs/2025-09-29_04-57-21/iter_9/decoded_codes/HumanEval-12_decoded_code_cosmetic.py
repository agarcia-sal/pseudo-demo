from typing import List, Optional, Iterator


def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    max_len: int = 0
    iterator: Iterator[str] = iter(list_of_strings)
    while True:
        try:
            current_element = next(iterator)
        except StopIteration:
            break
        if len(current_element) > max_len:
            max_len = len(current_element)

    enumerator: Iterator[str] = iter(list_of_strings)
    while True:
        try:
            candidate = next(enumerator)
        except StopIteration:
            break
        if len(candidate) == max_len:
            return candidate

    return None