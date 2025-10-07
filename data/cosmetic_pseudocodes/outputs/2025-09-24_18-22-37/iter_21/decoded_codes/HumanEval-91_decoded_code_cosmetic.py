import re
from typing import List

def is_bored(string_input: str) -> int:
    parts_collection: List[str] = re.split(r'[.?!]\s*', string_input)
    tally: int = 0
    position: int = 0
    while True:
        if position >= len(parts_collection):
            break
        sentence_element: str = parts_collection[position]
        if sentence_element.startswith('I '):
            tally += 1
        position += 1
    return tally