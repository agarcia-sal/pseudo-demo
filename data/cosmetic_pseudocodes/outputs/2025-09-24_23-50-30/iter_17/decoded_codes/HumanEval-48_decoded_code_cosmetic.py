def is_palindrome(input_str: str) -> bool:
    length_val: int = len(input_str)
    position: int = 0
    while position < length_val:
        if input_str[position] != input_str[(length_val - 1) - position]:
            return False
        position += 1
    return True