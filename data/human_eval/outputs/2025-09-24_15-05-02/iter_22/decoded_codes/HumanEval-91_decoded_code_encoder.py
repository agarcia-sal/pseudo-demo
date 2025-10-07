import re
from typing import List

def is_bored(input_string: str) -> int:
    # Split input_string by '.', '?', or '!' followed by optional whitespace
    sentences_list: List[str] = re.split(r'[.!?]\s*', input_string)
    boredom_count: int = 0
    for sentence in sentences_list:
        if sentence.startswith('I '):
            boredom_count += 1
    return boredom_count