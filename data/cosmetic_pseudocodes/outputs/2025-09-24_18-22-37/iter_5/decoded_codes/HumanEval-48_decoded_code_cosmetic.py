def is_palindrome(input_string: str) -> bool:
    length_value: int = len(input_string)
    position: int = 0
    while position < length_value:
        if input_string[position] == input_string[length_value - 1 - position]:
            position += 1
        else:
            return False
    return True