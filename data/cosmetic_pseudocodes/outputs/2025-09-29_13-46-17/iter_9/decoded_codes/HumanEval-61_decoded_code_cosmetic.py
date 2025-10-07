from typing import Tuple, Union


def correct_bracketing(string_of_brackets: str) -> bool:
    depth: int = 0

    def bracket_value(ch: str) -> int:
        return 1 if ch == "(" else -1

    def helper(depth: int, s: str) -> Tuple[Union[bool, int], int]:
        idx = 0
        while idx < len(s):
            v = bracket_value(s[idx])
            depth += v
            idx += 1
            if depth < 0:
                return False, idx
        return depth, idx

    result, _ = helper(depth, string_of_brackets)
    return result == 0