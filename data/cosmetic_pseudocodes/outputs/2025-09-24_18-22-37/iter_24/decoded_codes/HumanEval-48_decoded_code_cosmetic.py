def is_palindrome(string_input: str) -> bool:
    position: int = 0
    str_length: int = len(string_input)
    while position <= str_length - 1:
        front_char: str = string_input[position]
        back_char: str = string_input[str_length - 1 - position]
        if front_char == back_char:
            pass  # Continue loop
        else:
            return False
        position += 1
    return True