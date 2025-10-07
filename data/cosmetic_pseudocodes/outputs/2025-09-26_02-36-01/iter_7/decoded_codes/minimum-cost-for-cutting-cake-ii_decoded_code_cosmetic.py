from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        ZERO = 0
        ONE = 1
        LEN_HC = len(horizontalCut)
        LEN_VC = len(verticalCut)

        def DescendingSort(A: List[int]) -> None:
            # Bubble sort in descending order
            def Swap(idxA: int, idxB: int) -> None:
                A[idxA], A[idxB] = A[idxB], A[idxA]

            for idxOuter in range(LEN_HC + LEN_VC, ONE - 1, -1):
                for idxInner in range(ONE - 1, idxOuter - 1):
                    if A[idxInner] < A[idxInner + ONE]:
                        Swap(idxInner, idxInner + ONE)

        DescendingSort(horizontalCut)
        DescendingSort(verticalCut)

        costAccumulator = ZERO
        idxHorizontal = ZERO
        idxVertical = ZERO
        heightSegments = ONE
        widthSegments = ONE

        def ProcessCuts(x: int, y: int) -> bool:
            if x == LEN_VC:
                return False
            if y == LEN_HC:
                return True
            return horizontalCut[y] > verticalCut[x]

        def RecursiveCutAccumulation(hIdx: int, vIdx: int, hCount: int, vCount: int, acc: int) -> int:
            if hIdx >= LEN_HC and vIdx >= LEN_VC:
                return acc

            if ProcessCuts(vIdx, hIdx):
                return RecursiveCutAccumulation(
                    hIdx + ONE, vIdx, hCount + ONE, vCount, acc + horizontalCut[hIdx] * vCount
                )
            else:
                return RecursiveCutAccumulation(
                    hIdx, vIdx + ONE, hCount, vCount + ONE, acc + verticalCut[vIdx] * hCount
                )

        return RecursiveCutAccumulation(idxHorizontal, idxVertical, heightSegments, widthSegments, costAccumulator)