from typing import List

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        t = len(nums)
        u = [[0] * t for _ in range(t)]
        v = [[0] * t for _ in range(t)]

        def xorCompute(a: int, b: int) -> int:
            return a ^ b

        def maxCompute(a: int, b: int, c: int) -> int:
            if a >= b and a >= c:
                return a
            elif b >= c:
                return b
            else:
                return c

        def processIndex(w: int) -> None:
            if w < 0:
                return
            u[w][w] = nums[w]
            v[w][w] = nums[w]

            def iteratej(x: int) -> None:
                if x >= t:
                    return
                u[w][x] = xorCompute(u[w][x - 1], u[w + 1][x])
                v[w][x] = maxCompute(u[w][x], v[w][x - 1], v[w + 1][x])
                iteratej(x + 1)

            iteratej(w + 1)
            processIndex(w - 1)

        processIndex(t - 1)

        result = []
        m = 0
        while m < len(queries):
            l, r = queries[m]
            result.append(v[l][r])
            m += 1

        return result