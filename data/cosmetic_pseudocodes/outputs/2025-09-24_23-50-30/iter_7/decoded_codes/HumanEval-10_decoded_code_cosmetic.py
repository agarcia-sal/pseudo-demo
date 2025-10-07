from typing import Sequence

def is_palindrome(str_val: str) -> bool:
    def check(chars: str, L: int, R: int) -> bool:
        if L >= R:
            return True
        if chars[L] != chars[R]:
            return False
        return check(chars, L + 1, R - 1)
    return check(str_val, 0, len(str_val) - 1)

def make_palindrome(seq: str) -> str:
    def find_prefix_index(idx: int) -> int:
        if idx >= len(seq):
            return len(seq)
        if is_palindrome(seq[idx:]):
            return idx
        return find_prefix_index(idx + 1)

    if len(seq) == 0:
        return ""

    pos = find_prefix_index(0)
    prefix = seq[:pos]

    reversed_prefix = ""
    for i in range(len(prefix) - 1, -1, -1):
        reversed_prefix += prefix[i]

    return seq + reversed_prefix