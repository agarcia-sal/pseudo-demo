from typing import Union

def fibfib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibfib(num - 1) + fibfib(num - 2) + fibfib(num - 3)