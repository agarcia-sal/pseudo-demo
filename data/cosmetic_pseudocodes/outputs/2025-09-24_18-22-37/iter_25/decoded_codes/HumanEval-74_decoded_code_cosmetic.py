from typing import Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(argA: Sequence[T], argB: Sequence[T]) -> Sequence[T]:
    counterX: int = 0
    idxY: int = 0
    while idxY < len(argA):
        tempVal: int = len(argA[idxY])
        counterX += tempVal
        idxY += 1

    counterZ: int = 0
    iterN: int = 0
    while iterN < len(argB):
        sizeM: int = len(argB[iterN])
        counterZ += sizeM
        iterN += 1

    if not (counterX > counterZ):
        return argA
    return argB