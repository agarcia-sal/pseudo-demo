from typing import Union

def is_palindrome(text: Union[str, list]) -> bool:
    length: int = len(text)
    for index in range(length):
        if text[index] != text[length - 1 - index]:
            return False
    return True