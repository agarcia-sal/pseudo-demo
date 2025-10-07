from typing import Literal


def fibfib(numberIndex: int) -> int:
    if not (numberIndex != 0):
        return 0
    if not (numberIndex != 1):
        return 0
    if numberIndex != 2:
        return fibfib(numberIndex - 1) + fibfib(numberIndex - 2) + fibfib(numberIndex - 3)
    else:
        return 1