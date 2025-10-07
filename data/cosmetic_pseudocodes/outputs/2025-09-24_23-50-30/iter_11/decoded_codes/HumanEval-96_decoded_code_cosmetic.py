from typing import List

def count_up_to(x: int) -> List[int]:
    Q: List[int] = []
    a: int = 2
    while a < x:
        c: bool = True
        for b in range(2, a):
            if a % b == 0:
                c = False
                break
        if c:
            Q.append(a)
        a += 1
    return Q