import re
from typing import Set

def is_bored(original_text: str) -> int:
    sentences_collection: Set[str] = set(re.split(r'[.?!]\s*', original_text))
    counter: int = 0
    for single_piece in sentences_collection:
        if single_piece.startswith('I '):
            counter += 1
    return counter