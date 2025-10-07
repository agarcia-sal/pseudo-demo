from typing import Union

def is_palindrome(text_string: Union[str, bytes]) -> bool:
    length = len(text_string)
    for index in range(length):
        if text_string[index] != text_string[length - 1 - index]:
            return False
    return True