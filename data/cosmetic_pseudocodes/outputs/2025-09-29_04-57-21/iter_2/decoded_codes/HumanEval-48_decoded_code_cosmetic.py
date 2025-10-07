def is_palindrome(text: str) -> bool:
    length_counter: int = len(text)
    position: int = 0
    while position < length_counter:
        if text[position] != text[length_counter - 1 - position]:
            return False
        position += 1
    return True