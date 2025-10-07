def is_palindrome(text: str) -> bool:
    lengthValue: int = len(text)
    position: int = 0
    while position < lengthValue:
        leftChar: str = text[position]
        rightChar: str = text[(lengthValue - 1) - position]
        if leftChar != rightChar:
            return False
        position += 1
    return True