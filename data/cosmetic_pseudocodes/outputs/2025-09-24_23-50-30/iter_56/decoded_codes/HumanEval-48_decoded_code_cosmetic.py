def is_palindrome(inputString: str) -> bool:
    y0: int = 0
    y1: int = len(inputString) - 1
    while y0 < y1:
        if inputString[y0] == inputString[y1]:
            y0 += 1
            y1 -= 1
        else:
            return False
    return True