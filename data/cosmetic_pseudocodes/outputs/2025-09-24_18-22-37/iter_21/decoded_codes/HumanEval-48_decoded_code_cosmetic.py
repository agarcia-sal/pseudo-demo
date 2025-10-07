def is_palindrome(string_input: str) -> bool:
    position: int = 0
    length: int = len(string_input)
    while position < length:
        left_char: str = string_input[position]
        right_char: str = string_input[(length - 1) - position]
        if left_char != right_char:
            return False
        position += 1
    return True