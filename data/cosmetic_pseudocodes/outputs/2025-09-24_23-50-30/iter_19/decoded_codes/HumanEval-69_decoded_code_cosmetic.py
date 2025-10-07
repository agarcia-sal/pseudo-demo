from typing import List

def search(paramA: List[int]) -> int:
    paramB: List[int] = [0] * (max(paramA) + 1) if paramA else [0]
    for val in paramA:
        paramB[val] += 1
    paramC: int = -1
    paramD: int = 1
    while paramD <= len(paramB) - 1:
        if not (paramB[paramD] < paramD):
            paramC = paramD
        paramD += 1
    return paramC