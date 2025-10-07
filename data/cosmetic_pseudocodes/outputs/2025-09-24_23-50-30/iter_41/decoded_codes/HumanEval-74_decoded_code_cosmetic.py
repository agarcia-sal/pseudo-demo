from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(preservedParamA: Sequence[Sequence], preservedParamB: Sequence[Sequence]) -> Sequence[Sequence]:
    accVarX: int = 0
    idxVarY: int = 0
    while idxVarY < len(preservedParamA):
        accVarX += len(preservedParamA[idxVarY])
        idxVarY += 1

    def inner_sum(iterList: Sequence[Sequence], accVal: int, pos: int) -> int:
        if pos == len(iterList):
            return accVal
        return inner_sum(iterList, accVal + len(iterList[pos]), pos + 1)

    accVarZ: int = inner_sum(preservedParamB, 0, 0)
    if not (accVarX > accVarZ):
        return preservedParamA
    return preservedParamB