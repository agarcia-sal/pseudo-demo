def is_palindrome(string: str) -> bool:
    length = len(string)
    position = 0
    while position < length / 2:
        if string[position] == string[length - 1 - position]:
            position += 1
        else:
            return False
    return True