def is_palindrome(text: str) -> bool:
    position: int = 0
    limit: int = len(text) - 1
    while position <= limit:
        start_char: str = text[position]
        end_char: str = text[limit - position]
        if start_char != end_char:
            return False
        position += 1
    return True