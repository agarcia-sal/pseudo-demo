def is_palindrome(text: str) -> bool:
    totalChars: int = len(text)
    currentIndex: int = 0

    while currentIndex < totalChars:
        frontChar: str = text[currentIndex]
        backChar: str = text[(totalChars - 1) - currentIndex]

        if frontChar != backChar:
            return False

        currentIndex += 1

    return True