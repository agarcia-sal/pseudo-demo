import re
from typing import List


def is_bored(string_of_words: str) -> int:
    list_of_sentences: List[str] = re.split(r'[.?!]\s*', string_of_words)
    boredom_count: int = 0
    for sentence in list_of_sentences:
        if sentence.startswith('I '):
            boredom_count += 1
    return boredom_count