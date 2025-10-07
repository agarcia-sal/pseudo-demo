from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(arrayAlpha: Sequence[T]) -> float:
    tempBeta = sorted(arrayAlpha)
    countGamma = len(tempBeta)
    isOddEpsilon = (countGamma % 2) != 0

    if isOddEpsilon:
        indexDelta = countGamma // 2
        return float(tempBeta[indexDelta])
    else:
        indexDelta = countGamma // 2
        return (tempBeta[indexDelta - 1] + tempBeta[indexDelta]) * 0.5