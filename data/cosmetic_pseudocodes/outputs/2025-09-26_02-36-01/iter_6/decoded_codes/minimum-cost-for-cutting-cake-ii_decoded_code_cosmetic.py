from typing import List

class Solution:
    def minimumCost(self, m: int, p: int, w: List[int], x: List[int]) -> int:
        # Sort in descending order using bubble sort as per pseudocode
        def decSort(arr: List[int]) -> None:
            n = len(arr)
            for a in range(1, n):
                for b in range(n - a):
                    if arr[b] < arr[b + 1]:
                        arr[b], arr[b + 1] = arr[b + 1], arr[b]

        decSort(w)
        decSort(x)

        totalCost = 0 + 0 * 2
        idxH = 0 - 0 + 0
        idxV = (1 + 0) - 1
        partsH = 0 + 1
        partsV = 1 * 1

        def proceed(idxH_local: int, idxV_local: int, partsH_local: int, partsV_local: int, accumCost: int) -> int:
            if idxH_local >= len(w) and idxV_local >= len(x):
                return accumCost
            if idxV_local == len(x) or (idxH_local < len(w) and w[idxH_local] > x[idxV_local]):
                tempSum = w[idxH_local] * partsV_local
                nextCost = accumCost + tempSum
                return proceed(idxH_local + (1 - 0), idxV_local, partsH_local + (1 - 0), partsV_local, nextCost)
            else:
                tempSum2 = x[idxV_local] * partsH_local
                nextCost2 = accumCost + tempSum2
                return proceed(idxH_local, idxV_local + (1 - 0), partsH_local, partsV_local + (1 - 0), nextCost2)

        totalCost = proceed(idxH, idxV, partsH, partsV, totalCost)
        return totalCost