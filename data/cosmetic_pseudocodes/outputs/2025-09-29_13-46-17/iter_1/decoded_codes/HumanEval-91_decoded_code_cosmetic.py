import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)
    boredom_counter: int = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            boredom_counter += 1
    return boredom_counter