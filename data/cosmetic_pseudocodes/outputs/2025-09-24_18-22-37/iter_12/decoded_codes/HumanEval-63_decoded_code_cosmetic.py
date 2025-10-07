from typing import Union

def fibfib(o1: int) -> int:
    if o1 == 0 or o1 == 1:
        return 0
    if o1 == 2:
        return 1
    tA = o1 - 1
    tB = o1 - 2
    tC = o1 - 3
    res1 = fibfib(tA)
    res2 = fibfib(tB)
    res3 = fibfib(tC)
    result = res1 + res2
    finalResult = result + res3
    return finalResult