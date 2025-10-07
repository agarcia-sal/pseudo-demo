def is_palindrome(phrase: str) -> bool:
    length_checker: int = len(phrase)
    idx: int = 0
    while idx < length_checker:
        front_char: str = phrase[idx]
        back_pos: int = length_checker - (1 + idx)
        back_char: str = phrase[back_pos]
        if front_char != back_char:
            return False
        idx += 1
    return True