from typing import Union


def is_palindrome(data: Union[str, list]) -> bool:
    """Check if data is a palindrome by recursively comparing pairs."""
    def check_pair(position: int) -> bool:
        if not (position < len(data)):
            return True
        if data[position] != data[len(data) - 1 - position]:
            return False
        return check_pair(position + 1)

    return check_pair(0)