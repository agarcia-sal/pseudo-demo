from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=object)

def common(sequenceA: Sequence[T], sequenceB: Sequence[T]) -> List[T]:
    accumulator = {}
    for indexA in range(len(sequenceA)):
        currentA = sequenceA[indexA]
        pointerB = 0
        while pointerB < len(sequenceB):
            if not (currentA != sequenceB[pointerB]):
                accumulator[currentA] = True
            pointerB += 1
    return sorted(accumulator.keys())