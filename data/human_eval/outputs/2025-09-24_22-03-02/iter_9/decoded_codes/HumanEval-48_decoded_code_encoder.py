def is_palindrome(TEXT: str) -> bool:
    for i in range(len(TEXT)):
        if TEXT[i] != TEXT[len(TEXT) - 1 - i]:
            return False
    return True