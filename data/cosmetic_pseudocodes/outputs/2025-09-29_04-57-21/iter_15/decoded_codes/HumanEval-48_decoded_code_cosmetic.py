def is_palindrome(text: str) -> bool:
    position: int = 0
    length: int = len(text)
    while position < length / 2:
        front_char: str = text[position]
        rear_char: str = text[length - 1 - position]
        if front_char == rear_char:
            position += 1
            continue
        else:
            return False
    return True