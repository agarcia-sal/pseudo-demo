from typing import List

class Solution:
    def minChanges(self, uv: List[int]) -> int:
        n = len(uv)
        max_val = n // 2
        globz = [0] * (max_val + 3)  # length = length(uv)//2 + 2 + 1

        def incElem(arr: List[int], idx: int) -> None:
            arr[idx] += 1

        def decElem(arr: List[int], idx: int) -> None:
            arr[idx] -= 1

        def maxInt(a: int, b: int) -> int:
            return a if a > b else b

        floop = 0
        half = n // 2
        while floop <= half - 1:
            t1 = uv[floop]
            t2 = uv[n - floop - 1]
            if t1 > t2:
                t1, t2 = t2, t1

            incElem(globz, 0)
            decElem(globz, t2 - t1)
            incElem(globz, (t2 - t1) + 1)
            decElem(globz, maxInt(t2, half) - t1 + 1)
            incElem(globz, maxInt(t2, half) - t1 + 2)

            floop += 1

        accSum = 0
        minVal = None
        for val in globz:
            accSum += val
            if minVal is None or accSum < minVal:
                minVal = accSum

        return minVal