def is_palindrome(inputstr: str) -> bool:
    cursor: int = 0
    length: int = len(inputstr)
    while cursor < length:
        if inputstr[cursor] != inputstr[length - 1 - cursor]:
            return False
        cursor += 1
    return True