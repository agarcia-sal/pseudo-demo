from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    maxlen = 0
    for i in range(len(strings)):
        current_length = len(strings[i])
        if current_length > maxlen:
            maxlen = current_length
    for j in range(len(strings)):
        current_string = strings[j]
        current_length = len(current_string)
        if current_length == maxlen:
            return current_string