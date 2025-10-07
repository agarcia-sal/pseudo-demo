import re
from typing import List

def is_bored(S: str) -> int:
    if not isinstance(S, str):
        raise ValueError("Input must be a string")
    # Split input string into sentences using regex pattern "[.?!]\s*"
    sentences: List[str] = re.split(r"[.?!]\s*", S)
    boredom_count: int = 0
    for sentence in sentences:
        if sentence.startswith("I "):
            boredom_count += 1
    return boredom_count