def is_palindrome(str: str) -> bool:
    lenStr: int = len(str)
    pos: int = 0
    while pos < lenStr // 2:
        leftChar: str = str[pos]
        rightChar: str = str[lenStr - 1 - pos]
        if leftChar != rightChar:
            return False
        pos += 1
    return True