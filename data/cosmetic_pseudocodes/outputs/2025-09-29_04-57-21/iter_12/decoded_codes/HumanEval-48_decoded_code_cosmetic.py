def is_palindrome(text: str) -> bool:
    position: int = 0
    limit: int = len(text) - 1

    while position <= limit:
        left_char: str = text[position]
        right_char: str = text[limit - position]

        if left_char != right_char:
            return False

        position += 1

    return True