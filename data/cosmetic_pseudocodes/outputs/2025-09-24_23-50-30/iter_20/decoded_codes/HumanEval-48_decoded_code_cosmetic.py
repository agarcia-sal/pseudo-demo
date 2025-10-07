def is_palindrome(inputString: str) -> bool:
    position: int = 0
    length: int = len(inputString)
    while position < length:
        if inputString[position] != inputString[length - 1 - position]:
            return False
        position += 1
    return True