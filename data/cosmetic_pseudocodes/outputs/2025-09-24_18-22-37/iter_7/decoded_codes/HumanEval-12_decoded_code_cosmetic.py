from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    max_len: int = 0
    idx: int = 0
    while idx < len(array_of_texts):
        current_string: str = array_of_texts[idx]
        current_length: int = len(current_string)
        if current_length > max_len:
            max_len = current_length
        idx += 1

    j: int = 0
    while j < len(array_of_texts):
        candidate: str = array_of_texts[j]
        candidate_length: int = len(candidate)
        if candidate_length == max_len:
            return candidate
        else:
            j += 1