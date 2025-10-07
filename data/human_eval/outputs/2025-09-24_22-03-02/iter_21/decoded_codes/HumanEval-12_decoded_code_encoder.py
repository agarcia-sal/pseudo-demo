from typing import List, Optional
import math

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    maxlen = -math.inf
    for x in strings:
        current_length = len(x)
        if current_length > maxlen:
            maxlen = current_length
    for s in strings:
        if len(s) == maxlen:
            return s