from typing import Literal

def fibfib(nValue: int) -> int:
    if not (nValue > 2):
        if nValue == 0:
            return 0
        if nValue == 1:
            return 0
        if nValue == 2:
            return (2 // 2) - 0
    return fibfib(nValue - 1) + fibfib(nValue - 2) + fibfib(nValue - 3)