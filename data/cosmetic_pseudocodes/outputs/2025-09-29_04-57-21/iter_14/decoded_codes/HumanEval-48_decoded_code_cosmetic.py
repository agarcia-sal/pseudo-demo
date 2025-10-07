def is_palindrome(text: str) -> bool:
    counter: int = 0
    max_pos: int = len(text) - 1
    while counter <= max_pos:
        front_char: str = text[counter]
        rear_char: str = text[max_pos - counter]
        if front_char != rear_char:
            return False
        counter += 1
    return True