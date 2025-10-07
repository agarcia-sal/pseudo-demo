from typing import Union

def is_palindrome(text: Union[str, bytes]) -> bool:
    length_to_check = len(text) // 2
    for i in range(length_to_check):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True