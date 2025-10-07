def is_palindrome(text: str) -> bool:
    limit: int = len(text) // 2
    position: int = 0
    while position < limit:
        if text[position] == text[len(text) - 1 - position]:
            position += 1
        else:
            return False
    return True