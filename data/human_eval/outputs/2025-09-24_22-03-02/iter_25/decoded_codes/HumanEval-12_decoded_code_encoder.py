from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if len(strings) == 0:
        return None
    maxlen = 0
    for i in range(len(strings)):
        current_length = len(strings[i])
        if current_length > maxlen:
            maxlen = current_length
    for j in range(len(strings)):
        if len(strings[j]) == maxlen:
            return strings[j]