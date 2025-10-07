from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDesc(arr: List[int]) -> None:
            def quickSortDesc(low: int, high: int) -> None:
                if low < high:
                    pivotVal = arr[high]
                    idx = low
                    k = low
                    while k < high:
                        if arr[k] > pivotVal:
                            arr[k], arr[idx] = arr[idx], arr[k]
                            idx += 1
                        k += 1
                    arr[high], arr[idx] = arr[idx], arr[high]
                    quickSortDesc(low, idx - 1)
                    quickSortDesc(idx + 1, high)
            quickSortDesc(0, len(arr) - 1)

        sortDesc(horizontalCut)
        sortDesc(verticalCut)

        totalCost = 0
        posH = 0
        posV = 0
        countH = 1
        countV = 1

        def recur(i: int, j: int) -> None:
            nonlocal totalCost, posH, posV, countH, countV

            cond1 = (j == n - 1)
            cond2 = (i < m - 1)
            cond3 = (horizontalCut[i] > verticalCut[j])

            if cond1 or (cond2 and cond3):
                costAdd = horizontalCut[i] * countV
                totalCost += costAdd
                countH += 1
                posH = i + 1
                if not (posH < m - 1 or posV < n - 1):
                    return
                recur(posH, posV)
            else:
                costAdd = verticalCut[j] * countH
                totalCost += costAdd
                countV += 1
                posV = j + 1
                if not (posH < m - 1 or posV < n - 1):
                    return
                recur(posH, posV)

        recur(posH, posV)

        return totalCost