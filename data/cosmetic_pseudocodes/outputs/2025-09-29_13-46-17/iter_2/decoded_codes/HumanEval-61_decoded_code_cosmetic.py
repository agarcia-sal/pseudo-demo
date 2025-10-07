from typing import List


def correct_bracketing(string_of_brackets: str) -> bool:
    def recursive_check(chars: List[str], idx: int, current_depth: int) -> bool:
        if idx > len(chars) - 1:
            return current_depth == 0
        char = chars[idx]
        new_depth = current_depth + (1 if char == '(' else -1)
        if new_depth < 0:
            return False
        return recursive_check(chars, idx + 1, new_depth)

    return recursive_check(list(string_of_brackets), 0, 0)