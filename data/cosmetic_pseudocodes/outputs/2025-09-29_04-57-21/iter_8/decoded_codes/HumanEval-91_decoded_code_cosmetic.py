import re
from typing import List


def is_bored(input_string: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', input_string)
    count_bored: int = 0
    iterator: int = 0

    while iterator < len(sentence_collection):
        current_text: str = sentence_collection[iterator]
        if current_text.startswith('I '):
            count_bored += 1
        iterator += 1

    return count_bored