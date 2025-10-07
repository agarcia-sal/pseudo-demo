import re
from typing import Union

def is_bored(input_string: str) -> int:
    sentences: list[str] = re.split(r'[.?!]\s*', input_string)
    boredom_count: int = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            boredom_count += 1
    return boredom_count