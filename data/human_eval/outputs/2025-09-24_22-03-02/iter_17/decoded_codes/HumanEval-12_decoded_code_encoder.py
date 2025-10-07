from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if len(strings) == 0:
        return None
    maxlen = float('-inf')
    for x in strings:
        if len(x) > maxlen:
            maxlen = len(x)
    for s in strings:
        if len(s) == maxlen:
            return s