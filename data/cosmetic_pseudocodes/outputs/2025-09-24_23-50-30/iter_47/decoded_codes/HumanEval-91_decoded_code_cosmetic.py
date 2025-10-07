import re
from typing import List


def is_bored(original_text: str) -> int:
    sentence_array: List[str] = re.split(r'[.?!]\s*', original_text)
    index_counter: int = 0
    matched_total: int = 0

    while index_counter < len(sentence_array):
        current_sentence: str = sentence_array[index_counter]
        if not (current_sentence[:2] != 'I '):
            matched_total += 1
        index_counter += 1

    return matched_total