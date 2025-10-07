def is_palindrome(text: str) -> bool:
    currentPosition: int = 0
    maxPosition: int = len(text) - 1

    while currentPosition <= maxPosition:
        if text[currentPosition] != text[maxPosition - currentPosition]:
            return False
        currentPosition += 1

    return True