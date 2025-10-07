from typing import List, Optional

def longest(array_of_words: List[str]) -> Optional[str]:
    if len(array_of_words) == 0:
        return None

    max_len: int = 0
    idx: int = 0

    while idx < len(array_of_words):
        word_len = len(array_of_words[idx])
        if word_len > max_len:
            max_len = word_len
        idx += 1

    idx = 0
    while idx < len(array_of_words):
        if len(array_of_words[idx]) == max_len:
            candidate: str = array_of_words[idx]
            return candidate
        idx += 1

    return None