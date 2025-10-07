from typing import List

def get_odd_collatz(a: int) -> List[int]:
    b: List[int] = [] if a % 2 == 0 else [a]
    while a > 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a * 3 + 1
        if a % 2 != 0:
            b.append(a)
    return sorted(b)