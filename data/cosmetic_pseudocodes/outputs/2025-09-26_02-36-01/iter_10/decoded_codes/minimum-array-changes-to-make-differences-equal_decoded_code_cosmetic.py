from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        def addValue(lst: List[int], idx: int, val: int) -> None:
            lst[idx] += val

        def subValue(lst: List[int], idx: int, val: int) -> None:
            lst[idx] -= val

        def sumPrefix(arr: List[int]) -> int:
            def recursePrefix(arr: List[int], i: int, acc: int) -> int:
                if i >= len(arr):
                    return acc
                return recursePrefix(arr, i + 1, acc + arr[i])
            return recursePrefix(arr, 0, 0)

        d = [0] * (k + 2)
        n = len(nums)

        def loopProcess(idx: int) -> None:
            if idx > (n // 2) - 1:
                return

            a = nums[idx]
            b = nums[(n - 1) - idx]

            def orderPair(x: int, y: int) -> tuple[int, int]:
                if x > y:
                    return y, x
                return x, y

            p, q = orderPair(a, b)

            addValue(d, 0, 1)
            subValue(d, q - p, 1)
            addValue(d, (q - p) + 1, 1)
            subValue(d, max(q, k - p) + 1, 1)
            addValue(d, max(q, k - p) + 2, 1)

            loopProcess(idx + 1)

        loopProcess(0)

        def accumulate(arr: List[int]) -> List[int]:
            acc = 0
            result = [0] * len(arr)
            for j in range(len(arr)):
                acc += arr[j]
                result[j] = acc
            return result

        accumulated = accumulate(d)

        mini = accumulated[0]
        for z in range(1, len(accumulated)):
            if accumulated[z] < mini:
                mini = accumulated[z]

        return mini