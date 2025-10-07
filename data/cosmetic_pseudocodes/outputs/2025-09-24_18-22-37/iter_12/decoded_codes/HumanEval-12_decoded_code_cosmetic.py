from typing import List, Optional

def longest(array_of_words: List[str]) -> Optional[str]:
    if not array_of_words:
        return None

    max_len: int = 0
    idx: int = 0
    while idx < len(array_of_words):
        current_word: str = array_of_words[idx]
        current_length: int = len(current_word)
        if current_length > max_len:
            max_len = current_length
        idx += 1

    for idx in range(len(array_of_words)):
        candidate: str = array_of_words[idx]
        if len(candidate) == max_len:
            return candidate