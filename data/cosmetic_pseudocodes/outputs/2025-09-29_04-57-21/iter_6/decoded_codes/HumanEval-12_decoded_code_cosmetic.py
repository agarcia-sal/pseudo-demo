from typing import Optional, Iterable

def longest(words_collection: Iterable[str]) -> Optional[str]:
    words_list = list(words_collection)
    if not words_list:
        return None

    max_size: int = float('-inf')
    for element in words_list:
        length = len(element)
        if length > max_size:
            max_size = length

    for candidate in words_list:
        if len(candidate) == max_size:
            return candidate