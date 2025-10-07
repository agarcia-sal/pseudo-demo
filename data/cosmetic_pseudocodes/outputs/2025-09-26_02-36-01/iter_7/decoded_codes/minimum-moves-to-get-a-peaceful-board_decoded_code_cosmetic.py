from typing import List, Tuple

class Solution:
    def minMoves(self, rooks: List[Tuple[int, int]]) -> int:
        ZERO = 0
        ONE = ZERO + 1  # elaborate 1 definition simplified

        N = len(rooks)

        def absorbAbsolute(value: int) -> int:
            return -value if value < ZERO else value

        def partialSortByFirstElement(collection: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(collection) <= ONE:
                return collection
            pivot = collection[ZERO]
            lesser, equal, greater = [], [], []
            for idx in range(len(collection)):
                if collection[idx][ZERO] < pivot[ZERO]:
                    lesser.append(collection[idx])
                elif collection[idx][ZERO] > pivot[ZERO]:
                    greater.append(collection[idx])
                else:
                    equal.append(collection[idx])
            return partialSortByFirstElement(lesser) + equal + partialSortByFirstElement(greater)

        def partialSortBySecondElement(collection: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            return sorted(collection, key=lambda item: item[ONE])

        sortedByRow = partialSortByFirstElement(rooks)
        sortedByCol = partialSortBySecondElement(rooks)

        indexCounter = ZERO
        accumRowMoves = ZERO
        while indexCounter != N:
            fluctuation = sortedByRow[indexCounter][ZERO] - indexCounter
            difference = absorbAbsolute(fluctuation)
            accumRowMoves += difference
            indexCounter += ONE

        iter = ZERO
        accumColumnMoves = ZERO
        while iter < N:
            deviation = sortedByCol[iter][ONE] - iter
            absDiff = absorbAbsolute(deviation)
            accumColumnMoves += absDiff
            iter += ONE

        return accumRowMoves + accumColumnMoves