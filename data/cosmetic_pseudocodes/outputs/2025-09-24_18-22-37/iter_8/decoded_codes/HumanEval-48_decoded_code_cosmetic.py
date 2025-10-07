def is_palindrome(str_input: str) -> bool:
    pos: int = 0
    max_index: int = len(str_input) - 1
    while pos <= max_index:
        left_char: str = str_input[pos]
        right_pos: int = max_index - pos
        right_char: str = str_input[right_pos]
        if left_char != right_char:
            return False
        pos += 1
    return True