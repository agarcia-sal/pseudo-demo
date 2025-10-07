from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if len(strings) == 0:
        return None

    maxlen = 0
    for s in strings:
        current_length = len(s)
        if current_length > maxlen:
            maxlen = current_length

    for s in strings:
        if len(s) == maxlen:
            return s