from typing import Callable

def is_palindrome(text: str) -> bool:
    def check_symmetry(position: int, max_position: int) -> bool:
        if position >= max_position:
            return True
        left_char = text[position]
        right_char = text[(max_position * 2) - position]
        if left_char == right_char:
            return check_symmetry(position + 1, max_position)
        return False

    cutoff_point = len(text) // 2
    return check_symmetry(0, cutoff_point - 1)