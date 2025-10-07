from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDesc(arr: List[int]) -> None:
            idxMax = 0
            while True:
                swapped = False
                idxMax = len(arr) - 1
                u = 0
                while u < idxMax:
                    if arr[u] < arr[u + 1]:
                        arr[u], arr[u + 1] = arr[u + 1], arr[u]
                        swapped = True
                    u += 1
                if not swapped:
                    break

        sortDesc(horizontalCut)
        sortDesc(verticalCut)

        totalPrice = 0
        pointerH = 0
        pointerV = 0
        countH = 1
        countV = 1

        def isStillCutNeeded() -> bool:
            return (pointerH < (m - 1)) or (pointerV < (n - 1))

        def horizontalGreater() -> bool:
            return (pointerH < (m - 1)) and (horizontalCut[pointerH] > verticalCut[pointerV])

        while True:
            if not isStillCutNeeded():
                break

            if (pointerV == (n - 1)) or horizontalGreater():
                partCost = horizontalCut[pointerH] * countV
                totalPrice += partCost
                countH += 1
                pointerH += 1
            else:
                partCost = verticalCut[pointerV] * countH
                totalPrice += partCost
                countV += 1
                pointerV += 1

        return totalPrice