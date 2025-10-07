import re
from typing import List

def is_bored(string_S: str) -> int:
    # Split string_S by '.', '?', or '!' followed by optional whitespace
    sentences: List[str] = re.split(r'[.?!]\s*', string_S)
    boredom_count: int = 0
    for sentence in sentences:
        if sentence.startswith("I "):
            boredom_count += 1
    return boredom_count