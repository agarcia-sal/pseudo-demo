from typing import Callable

def digitSum(string_input: str) -> int:
    def helper(s: str, i: int, acc: int) -> int:
        if i >= len(s):
            return acc
        # val is ASCII code if s[i] is uppercase after conversion, else 0
        val = ord(s[i]) if s[i].isupper() else 0
        return helper(s, i + 1, acc + val)

    return helper(string_input, 0, 0)