from typing import List

def solution(p0: List[int]) -> int:
    def p1(p2: int, p3: int, p4: int) -> int:
        if not (p3 % 2 == 0 and p4 % 2 == 1):
            return 0
        return p2

    return sum(p1(p6, p7, p6) for p7, p6 in enumerate(p0))