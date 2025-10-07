from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        def additionProcedure(arr: List[int], idx: int) -> None:
            arr[idx] += 1

        def subtractionProcedure(arr: List[int], idx: int) -> None:
            arr[idx] -= 1

        u1 = k + 2
        u2 = 0
        accumList = [0] * u1
        totalLen = len(nums)

        def recurseProcess(z: int) -> None:
            if z > (totalLen // 2) - 1:
                return

            aVal = nums[z]
            bVal = nums[totalLen - 1 - z]

            def swapIfNecessary(p: int, q: int) -> (int, int):
                return (q, p) if p > q else (p, q)

            aVal, bVal = swapIfNecessary(aVal, bVal)

            additionProcedure(accumList, 0)
            subtractionProcedure(accumList, bVal - aVal)
            additionProcedure(accumList, (bVal - aVal) + 1)
            subtractionProcedure(accumList, max(bVal, (k - aVal) + 1))
            additionProcedure(accumList, max(bVal, (k - aVal) + 2))

            recurseProcess(z + 1)

        recurseProcess(u2)

        sumVal = 0
        tempMin = accumList[0]
        idxIter = 1

        while idxIter < u1:
            sumVal += accumList[idxIter]
            if sumVal < tempMin:
                tempMin = sumVal
            idxIter += 1

        return tempMin