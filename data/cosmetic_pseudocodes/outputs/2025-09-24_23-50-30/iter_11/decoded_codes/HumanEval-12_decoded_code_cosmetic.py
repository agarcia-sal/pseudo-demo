from typing import List, Optional

def longest(arr_strings: List[str]) -> Optional[str]:
    if arr_strings:
        max_len: int = float('-inf')
        for idx in range(len(arr_strings)):
            curr_len = len(arr_strings[idx])
            if max_len < curr_len:
                max_len = curr_len
        pos = 0
        while pos < len(arr_strings):
            if len(arr_strings[pos]) == max_len:
                return arr_strings[pos]
            pos += 1
    else:
        return None