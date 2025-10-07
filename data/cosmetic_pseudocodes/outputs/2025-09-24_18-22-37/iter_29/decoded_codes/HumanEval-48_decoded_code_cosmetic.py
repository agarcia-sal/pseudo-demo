def is_palindrome(input_str: str) -> bool:
    pos: int = 0
    length: int = len(input_str)
    while pos < length:
        if input_str[pos] != input_str[length - 1 - pos]:
            return False
        pos += 1
    return True