def is_palindrome(input_string: str) -> bool:
    position: int = 0
    size: int = len(input_string)
    while position < size:
        corresponding_position: int = size - 1 - position
        if input_string[position] != input_string[corresponding_position]:
            return False
        position += 1
    return True