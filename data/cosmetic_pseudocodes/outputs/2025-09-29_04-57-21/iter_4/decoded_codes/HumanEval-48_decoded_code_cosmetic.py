from typing import AnyStr

def is_palindrome(text: AnyStr) -> bool:
    length_var: int = len(text)
    position: int = 0
    while position < length_var:
        front_char: str = text[position]
        back_char: str = text[length_var - 1 - position]
        if front_char != back_char:
            return False
        position += 1
    return True