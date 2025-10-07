import re
from typing import List


def is_bored(text_input: str) -> int:
    fragments_list: List[str] = re.split(r'[.?!]\s*', text_input)
    counter: int = 0
    for piece in fragments_list:
        if piece.startswith('I '):
            counter += 1
    return counter