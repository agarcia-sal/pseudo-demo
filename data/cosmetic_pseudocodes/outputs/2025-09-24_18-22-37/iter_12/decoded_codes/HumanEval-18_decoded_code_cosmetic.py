def how_many_times(p1: str, p2: str) -> int:
    p3: int = len(p1)
    p4: int = len(p2)
    p5: int = 0
    p6: int = 0
    p7: int = p3 - p4
    while p6 <= p7:
        p8: str = p1[p6 : p6 + p4]
        if p8 == p2:
            p5 += 1
        p6 += 1
    return p5