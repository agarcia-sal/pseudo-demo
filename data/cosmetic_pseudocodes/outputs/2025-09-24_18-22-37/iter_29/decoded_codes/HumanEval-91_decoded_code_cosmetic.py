import re
from typing import List

def is_bored(alpha: str) -> int:
    sentences_collection: List[str] = re.split(r'[.?!]\s*', alpha)
    tally: int = 0
    iterator: int = 0
    while iterator < len(sentences_collection):
        snippet: str = sentences_collection[iterator]
        prefix: str = snippet[:2]
        if prefix == 'I ':
            tally += 1
        iterator += 1
    return tally