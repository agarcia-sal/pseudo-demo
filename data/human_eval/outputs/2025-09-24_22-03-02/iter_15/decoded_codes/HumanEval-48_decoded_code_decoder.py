def is_palindrome(text: str) -> bool:
    for i in range(len(text) - 1):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True