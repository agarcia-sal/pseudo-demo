import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    for sentence in sentences:
        if sentence.startswith("I "):
            tally += 1
    return tally