import re
from typing import List

def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    boredom_total: int = 0
    for sentence in sentences_array:
        if sentence.startswith('I '):
            boredom_total += 1
    return boredom_total