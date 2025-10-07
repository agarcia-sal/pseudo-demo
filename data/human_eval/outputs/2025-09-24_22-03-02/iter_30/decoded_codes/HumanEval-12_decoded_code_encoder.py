from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if len(strings) == 0:
        return None

    maxlen = 0
    i = 0
    while i < len(strings):
        x = strings[i]
        current_length = 0
        j = 0
        while j < len(x):
            j += 1
            current_length += 1
        if current_length > maxlen:
            maxlen = current_length
        i += 1

    k = 0
    while k < len(strings):
        s = strings[k]
        length_s = 0
        l = 0
        while l < len(s):
            l += 1
            length_s += 1
        if length_s == maxlen:
            return s
        k += 1