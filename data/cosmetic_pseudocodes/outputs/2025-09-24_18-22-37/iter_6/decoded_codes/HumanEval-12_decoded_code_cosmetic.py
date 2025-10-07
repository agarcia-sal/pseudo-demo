from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    max_len: int = 0
    idx: int = 0

    while idx < len(array_of_texts):
        current_len = len(array_of_texts[idx])
        if current_len > max_len:
            max_len = current_len
        idx += 1

    position: int = 0

    while position < len(array_of_texts):
        if len(array_of_texts[position]) == max_len:
            return array_of_texts[position]
        else:
            position += 1