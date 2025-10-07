from typing import Callable

def is_palindrome(input_string: str) -> bool:
    def verify_position(current_index: int) -> bool:
        if current_index >= len(input_string) / 2:
            return True
        if input_string[current_index] == input_string[len(input_string) - 1 - current_index]:
            return verify_position(current_index + 1)
        return False
    return verify_position(0)