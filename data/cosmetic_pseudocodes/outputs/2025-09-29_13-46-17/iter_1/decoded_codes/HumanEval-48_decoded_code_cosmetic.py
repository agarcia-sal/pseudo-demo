def is_palindrome(text: str) -> bool:
    length = len(text)
    for position in range(length // 2):
        if text[position] != text[length - 1 - position]:
            return False
    return True