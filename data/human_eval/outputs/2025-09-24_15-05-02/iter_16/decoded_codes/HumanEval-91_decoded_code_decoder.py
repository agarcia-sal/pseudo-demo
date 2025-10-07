import re
from typing import List

def is_bored(S: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', S)
    boredom_count: int = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            boredom_count += 1
    return boredom_count