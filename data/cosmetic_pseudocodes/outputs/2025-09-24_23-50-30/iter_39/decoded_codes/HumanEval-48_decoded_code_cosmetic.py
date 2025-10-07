from typing import Sequence

def is_palindrome(alphabet: Sequence[str]) -> bool:
    alpha_length: int = len(alphabet)
    pointer: int = 0
    while pointer < alpha_length:
        front_char: str = alphabet[pointer]
        back_char: str = alphabet[alpha_length - 1 - pointer]
        if front_char != back_char:
            return False
        pointer += 1
    return True