def is_palindrome(text: str) -> bool:
    n: int = len(text)
    left: int = 0
    right: int = n - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True