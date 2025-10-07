def is_palindrome(input_str: str) -> bool:
    position: int = 0
    limit: int = (len(input_str) - 1) // 2 + 1
    while position < limit:
        if input_str[position] != input_str[len(input_str) - 1 - position]:
            return False
        position += 1
    return True