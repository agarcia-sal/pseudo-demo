from typing import Sequence

def is_palindrome(sample: Sequence[str]) -> bool:
    counter: int = 0
    length: int = len(sample)
    while counter < length:
        front_char: str = sample[counter]
        back_char: str = sample[length - 1 - counter]
        if front_char != back_char:
            return False
        counter += 1
    return True