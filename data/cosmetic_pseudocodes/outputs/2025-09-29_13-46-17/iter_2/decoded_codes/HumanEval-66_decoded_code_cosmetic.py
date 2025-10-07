from typing import Callable

def digitSum(string_input: str) -> int:
    def helper(index: int, total: int) -> int:
        if index >= len(string_input):
            return total
        current_char = string_input[index]
        char_value = ord(current_char) if current_char.isupper() else 0
        return helper(index + 1, total + char_value)
    return helper(0, 0)