def is_palindrome(input_string: str) -> bool:
    position: int = 0
    length: int = len(input_string)
    half_length: int = length // 2
    while position < half_length:
        if input_string[position] == input_string[length - 1 - position]:
            position += 1
        else:
            return False
    return True