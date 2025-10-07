from typing import Union


def fibfib(index: int) -> int:
    if index == 0 or index == 1:
        return 0
    if index == 2:
        return 1

    total = 0
    offset = 1
    while offset <= 3:
        total += fibfib(index - offset)
        offset += 1

    return total