from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def check_position(current_pos: int) -> bool:
        if current_pos >= len(input_string) // 2:
            return True
        if input_string[current_pos] == input_string[len(input_string) - 1 - current_pos]:
            return check_position(current_pos + 1)
        return False

    return check_position(0)