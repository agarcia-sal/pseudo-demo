def is_palindrome(input_string: str) -> bool:
    position: int = 0
    length: int = len(input_string)
    while position < length * 0.5:
        front_char: str = input_string[position]
        rear_char: str = input_string[length - 1 - position]
        if front_char != rear_char:
            return False
        position += 1
    return True