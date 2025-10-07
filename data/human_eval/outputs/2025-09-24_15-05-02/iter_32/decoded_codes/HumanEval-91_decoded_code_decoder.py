import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)
    boredom_count: int = sum(sentence.startswith('I ') for sentence in sentences if sentence)
    return boredom_count