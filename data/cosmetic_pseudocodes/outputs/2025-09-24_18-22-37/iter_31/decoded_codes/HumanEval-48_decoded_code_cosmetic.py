def is_palindrome(inputString: str) -> bool:
    position: int = 0
    totalLength: int = len(inputString)
    while position < totalLength:
        leftChar: str = inputString[position]
        rightChar: str = inputString[(totalLength - 1) - position]
        if leftChar != rightChar:
            return False
        position += 1
    return True