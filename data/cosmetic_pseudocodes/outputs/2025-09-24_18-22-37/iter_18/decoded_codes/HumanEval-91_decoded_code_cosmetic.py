import re
from typing import List

def is_bored(xyzzy: str) -> int:
    counter: int = 0
    temp_array: List[str] = re.split(r'[.?!]\s*', xyzzy)
    idx: int = 1
    while idx <= len(temp_array):
        current_piece: str = temp_array[idx - 1]
        if not current_piece.startswith('I '):
            pass
        else:
            counter += 1
        idx += 1
    return counter