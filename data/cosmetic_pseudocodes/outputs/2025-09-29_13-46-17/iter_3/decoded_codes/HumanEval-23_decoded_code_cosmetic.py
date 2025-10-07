from typing import Callable


def strlen(strVal: str) -> int:
    length_counter: int = 0

    def countChars(index: int) -> None:
        nonlocal length_counter
        if index == len(strVal):
            return
        length_counter += 1
        countChars(index + 1)

    countChars(0)
    return length_counter