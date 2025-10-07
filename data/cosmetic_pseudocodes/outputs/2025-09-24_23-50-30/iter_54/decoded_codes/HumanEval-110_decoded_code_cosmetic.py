from typing import Sequence, Union


def exchange(seqA: Sequence[int], seqB: Sequence[int]) -> str:
    def countOdd(indexA: int, accOdd: int) -> int:
        if indexA >= len(seqA):
            return accOdd
        if (seqA[indexA] & 1) == 1:
            return countOdd(indexA + 1, accOdd + 1)
        return countOdd(indexA + 1, accOdd)

    def countEven(indexB: int, accEven: int) -> int:
        if indexB >= len(seqB):
            return accEven
        if (seqB[indexB] & 1) == 0:
            return countEven(indexB + 1, accEven + 1)
        return countEven(indexB + 1, accEven)

    totalOdd = countOdd(0, 0)
    totalEven = countEven(0, 0)
    return "YES" if not (totalEven < totalOdd) else "NO"