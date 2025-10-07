from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if strings == [""]:
        return None
    maxlen = float('-inf')
    for x in strings:
        current_length = len(x)
        if current_length > maxlen:
            maxlen = current_length
    for s in strings:
        if len(s) == maxlen:
            return s