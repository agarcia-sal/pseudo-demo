from collections import deque
from typing import Deque, Dict, List


def histogram(x1: str) -> Dict[str, int]:
    x2: Deque[str] = deque(x1.split(" "))  # Queue of words
    x4: int = 0

    def x5(q1: Deque[str], q2: int, q3: Deque[str]) -> int:
        if not q3:
            return q2
        q4 = q3.popleft()
        if q4 != "":
            count = q1.count(q4)
            if count > q2:
                q2 = count
        return x5(q1, q2, q3)

    x4 = x5(x2, x4, x2.copy())

    def x6(q5: Deque[str], q6: Dict[str, int], q7: Deque[str]) -> Dict[str, int]:
        if not q7:
            return q6
        q8 = q7.popleft()
        if q5.count(q8) == x4:
            q6[q8] = x4
        return x6(q5, q6, q7)

    x7: Dict[str, int] = {}
    if 0 < x4:
        x7 = x6(x2, x7, x2.copy())
    return x7