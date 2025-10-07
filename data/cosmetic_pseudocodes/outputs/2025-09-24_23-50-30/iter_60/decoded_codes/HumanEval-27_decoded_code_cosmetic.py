from typing import Callable

def flip_case(alpha: str) -> str:
    def toggle_char(ch: str) -> str:
        if 'a' <= ch <= 'z':
            return chr(ord(ch) - (ord('a') - ord('A')))
        elif 'A' <= ch <= 'Z':
            return chr(ord(ch) + (ord('a') - ord('A')))
        else:
            return ch

    def recurse(idx: int, acc: str) -> str:
        if idx == len(alpha):
            return acc
        return recurse(idx + 1, acc + toggle_char(alpha[idx]))

    return recurse(0, "")