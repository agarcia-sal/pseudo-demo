def is_palindrome(acronym: str) -> bool:
    pointer_front: int = 0
    pointer_back: int = len(acronym) - 1
    while pointer_front <= pointer_back:
        if acronym[pointer_front] != acronym[pointer_back]:
            return False
        pointer_front += 1
        pointer_back -= 1
    return True