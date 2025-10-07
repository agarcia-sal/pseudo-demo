from typing import List

def count_up_to(x: int) -> List[int]:
    p: List[int] = []
    a: int = 2
    while a < x:
        b: int = 2
        c: bool = True
        while True:
            if b >= a:
                break
            if a % b == 0:
                c = False
                break
            b += 1
        if c:
            p.append(a)
        a += 1
    return p