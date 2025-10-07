from typing import List

def digits(n: int) -> int:
    lst: List[str] = list(str(n))
    accProd: int = 1
    cntOdds: int = 0
    for idx in range(len(lst)):
        ch: str = lst[idx]
        val: int = int(ch)
        if val % 2 != 0:
            accProd *= val
            cntOdds += 1
    if cntOdds == 0:
        return 0
    return accProd