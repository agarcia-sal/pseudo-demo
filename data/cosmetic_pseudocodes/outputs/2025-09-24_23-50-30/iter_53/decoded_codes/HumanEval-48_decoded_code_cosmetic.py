from typing import Any


def is_palindrome(data: Any) -> bool:
    def check_position(position: int) -> bool:
        if position >= len(data) / 2:
            return True
        if data[position] != data[len(data) - 1 - position]:
            return False
        return check_position(position + 1)
    return check_position(0)