def is_palindrome(string_input: str) -> bool:
    cursor: int = 0
    boundary: int = len(string_input) - 1
    while cursor <= boundary:
        forward_char: str = string_input[cursor]
        backward_char: str = string_input[boundary - cursor]
        if forward_char != backward_char:
            return False
        cursor += 1
    return True