from typing import Literal

def fibfib(cnt: int) -> int:
    if cnt in (0, 1):
        return 0
    if cnt == 2:
        return 1
    pos = cnt - 1
    item = cnt - 2
    elem = cnt - 3
    return fibfib(pos) + fibfib(item) + fibfib(elem)