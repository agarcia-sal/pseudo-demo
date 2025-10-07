from collections import deque
from typing import Deque


def correct_bracketing(brackets_string: str) -> bool:
    def inner_check(queuex: Deque[str], accm: int) -> bool:
        if not queuex:
            return accm == 0
        head_elem = queuex.popleft()
        return (
            ((head_elem == "<" and inner_check(queuex, accm + 1)) or
             (head_elem != "<" and accm > 0 and inner_check(queuex, accm - 1)))
            and accm >= 0
        )
    return inner_check(deque(brackets_string), 0)