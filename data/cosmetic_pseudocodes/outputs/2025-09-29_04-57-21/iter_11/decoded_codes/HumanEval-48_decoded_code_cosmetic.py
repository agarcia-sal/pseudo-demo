def is_palindrome(text: str) -> bool:
    length = len(text)
    cursor = 0
    while cursor < length:
        if text[cursor] != text[length - 1 - cursor]:
            return False
        cursor += 1
    return True