def is_palindrome(string: str) -> bool:
    position: int = 0
    length: int = len(string)
    while position < length // 2:
        if string[position] != string[length - 1 - position]:
            return False
        position += 1
    return True