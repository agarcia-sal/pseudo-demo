from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def descSort(arr: List[int]) -> List[int]:
            p = len(arr)
            q = 1
            while q <= len(arr):
                q += 1
                r = 1
                while r < p:
                    if arr[r - 1] < arr[r]:
                        arr[r - 1], arr[r] = arr[r], arr[r - 1]
                    r += 1
                p -= 1
            return arr

        sortedHor = descSort(horizontalCut[:])  # copy to avoid mutating input
        sortedVer = descSort(verticalCut[:])    # copy to avoid mutating input

        totalSum = 0
        idxH = 0
        idxV = 0
        sectionH = 1
        sectionV = 1

        while idxH < len(sortedHor) or idxV < len(sortedVer):
            if idxV == len(sortedVer):
                segCost = sortedHor[idxH] * sectionV
                totalSum += segCost
                sectionH += 1
                idxH += 1
                continue

            if idxH < len(sortedHor):
                if sortedHor[idxH] > sortedVer[idxV]:
                    segCost = sortedHor[idxH] * sectionV
                    totalSum += segCost
                    sectionH += 1
                    idxH += 1
                    continue
                else:
                    segCost = sortedVer[idxV] * sectionH
                    totalSum += segCost
                    sectionV += 1
                    idxV += 1
                    continue
            else:
                segCost = sortedVer[idxV] * sectionH
                totalSum += segCost
                sectionV += 1
                idxV += 1

        return totalSum