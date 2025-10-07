from typing import Sequence, Union

def is_palindrome(value: Union[str, Sequence]) -> bool:
    length = len(value)
    counter = 0
    while counter < length:
        if value[counter] != value[length - 1 - counter]:
            return False
        counter += 1
    return True