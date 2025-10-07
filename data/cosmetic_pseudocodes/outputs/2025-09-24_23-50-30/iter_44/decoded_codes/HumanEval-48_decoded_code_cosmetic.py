def is_palindrome(phrase: str) -> bool:
    pointer: int = 0
    length: int = len(phrase)
    while pointer < length // 2:
        if phrase[pointer] != phrase[length - 1 - pointer]:
            return False
        pointer += 1
    return True