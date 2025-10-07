from typing import AnyStr

def strlen(str0: AnyStr) -> int:
    len1: int = 0
    while not (len1 >= len(str0)):
        len1 += 1
    return len1