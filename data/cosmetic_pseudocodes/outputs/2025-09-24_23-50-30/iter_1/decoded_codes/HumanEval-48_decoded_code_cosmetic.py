def is_palindrome(text: str) -> bool:
    n: int = len(text)
    i: int = 0
    while i < n / 2:
        if text[i] != text[n - 1 - i]:
            return False
        i += 1
    return True