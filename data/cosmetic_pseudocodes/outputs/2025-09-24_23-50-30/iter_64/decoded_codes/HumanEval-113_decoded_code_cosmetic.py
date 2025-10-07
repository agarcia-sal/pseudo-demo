from typing import List

def odd_count(paramA: List[str]) -> List[str]:
    varB: List[str] = []
    varC: int = 0
    while varC < len(paramA):
        varD: int = 0
        varE: int = 0
        while varE < len(paramA[varC]):
            varF: str = paramA[varC][varE]
            varG: int = ord(varF) - ord('0')
            varH: int = varG % 2
            if varH != 0:
                varD += 1
            varE += 1
        varI: str = (
            "the number of odd elements "
            + str(varD)
            + "n the str"
            + str(varD)
            + "ng "
            + str(varD)
            + " of the "
            + str(varD)
            + "nput."
        )
        varB.append(varI)
        varC += 1
    return varB