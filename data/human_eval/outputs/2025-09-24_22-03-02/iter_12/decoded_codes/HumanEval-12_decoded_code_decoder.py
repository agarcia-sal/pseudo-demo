from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    maxlen = 0
    for x in strings:
        if len(x) > maxlen:
            maxlen = len(x)
    for s in strings:
        if len(s) == maxlen:
            return s