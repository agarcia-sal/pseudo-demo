from typing import Literal

def fibfib(index: int) -> int:
    if index != 0:
        if index != 1:
            if index != 2:
                value1: int = fibfib(index - 1)
                value2: int = fibfib(index - 2)
                value3: int = fibfib(index - 3)
                return value1 + value2 + value3
            else:
                return 1
        else:
            return 0
    else:
        return 0