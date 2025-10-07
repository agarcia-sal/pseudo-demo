from typing import Sequence, List, Any, Dict

def common(arrayA: Sequence[Any], sequenceB: Sequence[Any]) -> List[Any]:
    acc: Dict[Any, bool] = {}
    idxA = 0

    while idxA < len(arrayA):
        itemA = arrayA[idxA]
        idxB = 0

        while idxB < len(sequenceB):
            itemB = sequenceB[idxB]

            if not (itemA != itemB):
                acc[itemA] = True

            idxB += 1

        idxA += 1

    return sorted(acc.keys())