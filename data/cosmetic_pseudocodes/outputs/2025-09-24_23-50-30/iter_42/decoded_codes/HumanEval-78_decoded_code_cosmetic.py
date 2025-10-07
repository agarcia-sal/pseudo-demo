from typing import Set

def hex_key(string_num: str) -> int:
    s: str = string_num
    p: Set[str] = {'2', '3', '5', '7', 'B', 'D'}
    c: int = 0
    i: int = 0
    while i < len(s):
        if s[i] in p:
            c += 1
        i += 1
    return c