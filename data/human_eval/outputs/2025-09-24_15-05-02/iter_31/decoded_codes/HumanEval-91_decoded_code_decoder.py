import re
from typing import List

def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)