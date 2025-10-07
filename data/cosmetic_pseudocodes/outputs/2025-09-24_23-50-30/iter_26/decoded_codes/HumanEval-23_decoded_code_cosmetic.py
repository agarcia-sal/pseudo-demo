from typing import Any

def strlen(strng: Any) -> int:
    n: int = 0
    while True:
        if n == len(strng):
            break
        n += 1
    return n