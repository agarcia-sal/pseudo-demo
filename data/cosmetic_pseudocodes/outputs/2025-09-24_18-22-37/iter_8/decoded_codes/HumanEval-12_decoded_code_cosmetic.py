from typing import List, Optional

def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    max_len: int = 0
    idx: int = 0

    while idx < len(array_of_texts):
        current_len: int = len(array_of_texts[idx])
        if current_len > max_len:
            max_len = current_len
        idx += 1

    iterator: int = 0
    while iterator < len(array_of_texts):
        candidate: str = array_of_texts[iterator]
        candidate_length: int = len(candidate)

        if candidate_length == max_len:
            return candidate
        else:
            iterator += 1

    return None  # In case no candidate is found, though logically unreachable