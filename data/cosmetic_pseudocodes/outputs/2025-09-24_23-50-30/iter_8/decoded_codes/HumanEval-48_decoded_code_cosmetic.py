def is_palindrome(string: str) -> bool:
    length: int = len(string)
    position: int = 0
    while position < length // 2:
        if string[position] != string[length - (position + 1)]:
            return False
        position += 1
    return True