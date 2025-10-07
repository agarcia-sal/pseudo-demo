from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def computeSign(index: int, negCount: int) -> int:
        if index >= len(array_of_integers):
            return 1 if negCount % 2 == 0 else -1
        currentVal = array_of_integers[index]
        if currentVal == 0:
            return 0
        return computeSign(index + 1, negCount + 1 if currentVal < 0 else negCount)

    if not array_of_integers:
        return None

    totalAbs = sum(-x if x < 0 else x for x in array_of_integers)
    finalSign = computeSign(0, 0)
    return finalSign * totalAbs