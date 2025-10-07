def is_palindrome(inputStr: str) -> bool:
    idx: int = 0
    limit: int = len(inputStr)
    while idx < limit // 2:
        fromStart: str = inputStr[idx]
        fromEnd: str = inputStr[limit - (idx + 1)]
        if fromStart != fromEnd:
            return False
        idx += 1
    return True