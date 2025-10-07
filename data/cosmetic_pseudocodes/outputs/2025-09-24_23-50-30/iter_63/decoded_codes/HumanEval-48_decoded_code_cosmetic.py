def is_palindrome(text: str) -> bool:
    length = len(text)
    for pos in range(length // 2):
        if text[pos] != text[length - 1 - pos]:
            return False
    return True