import re
from typing import List

def is_bored(alphabet_sequence: str) -> int:
    array_of_phrases: List[str] = re.split(r'[?!.]\s*', alphabet_sequence)
    tally: int = 0
    idx: int = 0
    while idx < len(array_of_phrases):
        snippet: str = array_of_phrases[idx]
        prefix: str = snippet[:2]
        if prefix == 'I ':
            tally += 1
        idx += 1
    return tally