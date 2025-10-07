def is_palindrome(input_string: str) -> bool:
    position: int = 0
    limit: int = len(input_string) - 1
    while position <= limit / 2:
        if input_string[position] != input_string[limit - position]:
            return False
        position += 1
    return True