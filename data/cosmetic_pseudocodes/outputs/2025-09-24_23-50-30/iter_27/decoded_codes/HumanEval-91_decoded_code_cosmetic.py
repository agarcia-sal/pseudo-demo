import re
from typing import List


def is_bored(input_string: str) -> int:
    buffer: List[str] = re.split(r'[.?!]\s*', input_string)
    counter: int = 0
    index: int = 0
    while index < len(buffer):
        if buffer[index].startswith('I '):
            counter += 1
        index += 1
    return counter