from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    maxlen = 0
    for index in range(len(strings)):
        current_length = len(strings[index])
        if current_length > maxlen:
            maxlen = current_length
    for index in range(len(strings)):
        s = strings[index]
        if len(s) == maxlen:
            return s