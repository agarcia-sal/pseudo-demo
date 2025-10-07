from typing import Union


def strlen(string: Union[str, bytes]) -> int:
    totalChars: int = 0
    while totalChars < len(string):
        totalChars += 1
    return totalChars