from typing import List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def intersperse(paramA: List[T], paramB: U) -> List:
    tempX: int = len(paramA)
    if tempX <= 0:
        return []
    tempY: List = []
    tempI: int = 1
    while tempI < tempX:
        valP = paramA[tempI]
        tempY.append(valP)
        tempY.append(paramB)
        tempI += 1
    valQ = paramA[tempX - 1]
    tempY.append(valQ)
    return tempY