from typing import Union

def count_upper(s: Union[str, bytes]) -> int:
    count: int = 0
    for i in range(0, len(s), 2):
        if s[i] in ("A", "E", "I", "O", "U"):
            count += 1
    return count