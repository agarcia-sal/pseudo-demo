from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if strings == [""]:
        return None

    maxlen = 0
    for i in range(len(strings)):
        current_length = len(strings[i])
        if current_length > maxlen:
            maxlen = current_length

    for j in range(len(strings)):
        s = strings[j]
        s_length = len(s)
        if s_length == maxlen:
            return s