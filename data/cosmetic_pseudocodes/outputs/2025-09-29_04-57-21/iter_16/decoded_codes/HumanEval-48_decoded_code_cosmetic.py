def is_palindrome(text: str) -> bool:
    position: int = 0
    length: int = len(text)
    while position < length:
        if text[position] != text[length - 1 - position]:
            return False
        position += 1
    return True