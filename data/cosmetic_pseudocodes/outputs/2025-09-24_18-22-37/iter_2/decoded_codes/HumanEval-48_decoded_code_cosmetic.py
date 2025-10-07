def is_palindrome(input_string: str) -> bool:
    length: int = len(input_string)
    position: int = 0
    while position < length:
        if input_string[position] != input_string[length - 1 - position]:
            return False
        position += 1
    return True