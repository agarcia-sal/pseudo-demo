from typing import List, Optional

def rolling_max(p0: List[int]) -> List[Optional[int]]:
    p1: List[Optional[int]] = []
    p2: Optional[int] = None

    def p3(p4: int, p5: int) -> int:
        # Return p4 if p4 is p5 (same object), else p5
        if p4 is p5:
            return p4
        else:
            return p5

    def p7(p8: Optional[int], p9: int) -> int:
        # If p8 is None, return p9, else use p3 to decide
        if p8 is None:
            return p9
        else:
            return p3(p8, p9)

    def p10(p11: int, p12: int) -> int:
        # Return the greater of p11 and p12
        if p11 > p12:
            return p11
        else:
            return p12

    def p13(p14: List[int], p15: Optional[int], p16: int) -> List[Optional[int]]:
        if p16 == len(p14):
            return p1
        else:
            nonlocal p2
            p2 = p7(p15, p14[p16])
            p1.append(p2)
            return p13(p14, p2, p16 + 1)

    p1 = []
    return p13(p0, p2, 0)