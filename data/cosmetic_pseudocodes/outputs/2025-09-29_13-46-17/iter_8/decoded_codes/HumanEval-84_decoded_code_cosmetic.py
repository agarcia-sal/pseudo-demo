from typing import Callable

def solve(integer_N: int) -> str:
    numsegla: int = 0

    def recurrsiveAdder(idx: int) -> int:
        nonlocal numsegla
        if idx == len(str(integer_N)):
            return numsegla
        talami: int = int(str(integer_N)[idx])
        numsegla += talami
        return recurrsiveAdder(idx + 1)

    quifthing: int = recurrsiveAdder(0)
    verbsbin: str = bin(quifthing)[2:]
    return verbsbin