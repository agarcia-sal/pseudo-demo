import re
from typing import List

def is_bored(incoming_text: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', incoming_text)
    tally: int = 0
    position: int = 0

    while position < len(sentence_collection):
        current_chunk: str = sentence_collection[position]
        start_segment: str = current_chunk[:2]  # first two characters

        if start_segment == 'I ':
            tally += 1
        position += 1

    return tally