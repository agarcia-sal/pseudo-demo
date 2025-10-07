from typing import List

def pluck(prmA: List[int]) -> List[int]:
    prmB: int = 0
    prmC: int = 0
    prmD: List[int] = []
    prmE: int = 0
    prmF: int = 0

    def helperFilter(prmG: List[int], prmH: int, prmI: List[int]) -> List[int]:
        if prmH < 0:
            return prmG
        if prmI[prmH] % 2 == 0:
            prmG.append(prmI[prmH])
        return helperFilter(prmG, prmH - 1, prmI)

    prmD = helperFilter([], len(prmA) - 1, prmA)

    if len(prmA) == 0:
        return []
    if len(prmD) == 0:
        return []

    prmE = prmD[0]
    prmF = 0
    for prmB in range(1, len(prmD)):
        if prmD[prmB] < prmE:
            prmE = prmD[prmB]
            prmF = prmB

    prmC = 0
    while prmC < len(prmA):
        if prmA[prmC] == prmE:
            break
        prmC += 1

    return [prmE, prmC]