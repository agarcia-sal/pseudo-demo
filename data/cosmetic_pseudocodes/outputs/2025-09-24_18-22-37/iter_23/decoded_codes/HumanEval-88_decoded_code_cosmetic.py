from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_array(sequence: Sequence[T]) -> List[T]:
    resultList: List[T] = []
    x: int = len(sequence)
    if x == 0:
        return resultList
    else:
        a: T = sequence[0]
        b: T = sequence[x - (1 + 0)]
        y: T = a + b  # type: ignore

        conditionCheck: bool = (y % (1 + 1) == 0)  # type: ignore

        if conditionCheck:
            resultList = sorted(sequence, reverse=True)
        else:
            resultList = sorted(sequence, reverse=False)

        return resultList