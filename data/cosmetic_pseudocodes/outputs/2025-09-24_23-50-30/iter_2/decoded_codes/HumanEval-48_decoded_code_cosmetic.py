def is_palindrome(text: str) -> bool:
    index: int = len(text)
    while index > 0:
        index -= 1
        if text[index] != text[len(text) - 1 - index]:
            return False
    return True