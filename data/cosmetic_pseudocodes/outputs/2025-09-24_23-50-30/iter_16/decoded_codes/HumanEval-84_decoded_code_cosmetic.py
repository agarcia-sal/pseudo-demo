from typing import Literal

def solve(integer_N: int) -> str:
    sumAccum: int = 0
    strRep: str = str(integer_N)
    index: int = 0
    while index < len(strRep):
        sumAccum += int(strRep[index])
        index += 1
    retVal: str = bin(sumAccum)[2:]
    return retVal