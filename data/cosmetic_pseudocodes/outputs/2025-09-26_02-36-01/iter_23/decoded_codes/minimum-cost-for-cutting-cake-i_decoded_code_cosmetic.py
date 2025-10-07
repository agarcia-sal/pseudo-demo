class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        def DescendingSort(arr: list[int]) -> None:
            def QuickSortDesc(left: int, right: int) -> None:
                if left < right:
                    pivotIndex = left
                    partitionIndex = left

                    def Swap(x: int, y: int) -> None:
                        arr[x], arr[y] = arr[y], arr[x]

                    for k in range(left + 1, right + 1):
                        if arr[k] > arr[pivotIndex]:
                            partitionIndex += 1
                            Swap(partitionIndex, k)
                    Swap(pivotIndex, partitionIndex)
                    QuickSortDesc(left, partitionIndex - 1)
                    QuickSortDesc(partitionIndex + 1, right)

            QuickSortDesc(0, len(arr) - 1)

        DescendingSort(horizontalCut)
        DescendingSort(verticalCut)

        accumulator = 0
        idxHorizontal = 0
        idxVertical = 0
        countHorizontal = 1
        countVertical = 1

        def LoopUntilDone(a: int, b: int, c: int, d: int) -> None:
            nonlocal accumulator, idxHorizontal, idxVertical, countHorizontal, countVertical
            if not (a < m - 1 or b < n - 1):
                return
            if b == n - 1 or (a < m - 1 and horizontalCut[a] > verticalCut[b]):
                accumulator += horizontalCut[a] * d
                countHorizontal += 1
                idxHorizontal += 1
                LoopUntilDone(idxHorizontal, idxVertical, countHorizontal, countVertical)
            else:
                accumulator += verticalCut[b] * c
                countVertical += 1
                idxVertical += 1
                LoopUntilDone(idxHorizontal, idxVertical, countHorizontal, countVertical)

        LoopUntilDone(idxHorizontal, idxVertical, countHorizontal, countVertical)

        return accumulator