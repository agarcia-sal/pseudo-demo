from typing import List

def flip_case(gamma: str) -> str:
    ctrl: int = 0
    delta: List[str] = []
    while ctrl < len(gamma):
        ch: str = gamma[ctrl]
        if 'a' <= ch <= 'z':
            delta.append(chr(ord(ch) - (ord('a') - ord('A'))))
        elif 'A' <= ch <= 'Z':
            delta.append(chr(ord(ch) + (ord('a') - ord('A'))))
        else:
            delta.append(ch)
        ctrl += 1
    return ''.join(delta)