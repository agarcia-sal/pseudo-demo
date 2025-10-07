from typing import Union

def is_palindrome(text: Union[str, list]) -> bool:
    length = len(text)
    for i in range(length):
        if text[i] != text[length - 1 - i]:
            return False
    return True