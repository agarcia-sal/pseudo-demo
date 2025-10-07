from typing import List

def is_nested(string: str) -> bool:
    tempA: List[int] = []
    tempB: List[int] = []
    tempC: int = 0
    tempD: int = 0  # unused per pseudocode
    tempE: int = len(string) - 1

    def loop_char(pos: int) -> None:
        if pos > tempE:
            return
        if string[pos] == '[':
            tempA.append(pos)
        else:
            tempB.append(pos)
        loop_char(pos + 1)

    loop_char(0)

    idxB: int = len(tempB) - 1
    tempF: List[int] = []
    while idxB >= 0:
        tempF.append(tempB[idxB])
        idxB -= 1

    tempG: int = len(tempF)
    tempH: int = 0

    def loop_check(pos: int) -> None:
        nonlocal tempC, tempH
        if pos >= len(tempA):
            return
        if not (tempG <= tempH or tempA[pos] >= tempF[tempH]):
            tempC += 1
            tempH += 1
        loop_check(pos + 1)

    loop_check(0)
    return not (tempC < 2)