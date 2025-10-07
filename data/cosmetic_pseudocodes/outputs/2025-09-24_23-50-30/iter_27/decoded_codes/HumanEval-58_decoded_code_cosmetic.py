from typing import Sequence, List, Dict, TypeVar

T = TypeVar('T')

def common(sequenceA: Sequence[T], sequenceB: Sequence[T]) -> List[T]:
    accumulator: Dict[T, bool] = {}
    indexP: int = 0
    lenA = len(sequenceA)
    lenB = len(sequenceB)
    while indexP < lenA:
        indexQ: int = 0
        while indexQ < lenB:
            if sequenceA[indexP] == sequenceB[indexQ]:
                accumulator[sequenceA[indexP]] = True
                indexQ += 1  # move to next element in sequenceB after a match
                break        # exit inner loop as per pseudocode 'BREAK'
            else:
                indexQ += 1
        indexP += 1
    collected = list(accumulator.keys())
    return sorted(collected)