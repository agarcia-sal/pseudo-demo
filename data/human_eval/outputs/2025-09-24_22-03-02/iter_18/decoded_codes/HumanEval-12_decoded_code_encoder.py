from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if strings == [""]:
        return None
    maxlen = 0
    for index in range(len(strings)):
        current_string = strings[index]
        current_length = 0
        for char_index in range(len(current_string)):
            current_length += 1
        if current_length > maxlen:
            maxlen = current_length
    for index in range(len(strings)):
        s = strings[index]
        s_length = 0
        for char_index in range(len(s)):
            s_length += 1
        if s_length == maxlen:
            return s