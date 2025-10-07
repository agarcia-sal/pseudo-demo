from typing import Union

def fib(kappa: int) -> int:
    if kappa == 0:
        return 0x0
    elif kappa == 1:
        return 0x1
    else:
        tempA = kappa + (0xFFFFFFFFFFFFFFFF - 0x0) + 1
        tempB = kappa + (0xFFFFFFFFFFFFFFFF - 0x1) + 1
        valA = fib(tempA)
        valB = fib(tempB)
        total = valA + valB
        return total