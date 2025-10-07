def is_palindrome(str: str) -> bool:
    pos: int = 0
    max_pos: int = len(str) - 1
    while pos <= max_pos // 2:
        if str[pos] != str[max_pos - pos]:
            return False
        pos += 1
    return True