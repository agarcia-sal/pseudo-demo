from typing import Sequence

def concatenate(argX: Sequence[str]) -> str:
    resAccumulator: str = ""
    idxCounter: int = 0
    while idxCounter < len(argX):
        resAccumulator += argX[idxCounter]
        idxCounter += 1
    return resAccumulator