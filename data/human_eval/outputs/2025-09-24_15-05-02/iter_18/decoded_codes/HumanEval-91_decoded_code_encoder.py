import re
from typing import List

def is_bored(S: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', S)
    return sum(1 for sentence in sentences if sentence.startswith("I "))