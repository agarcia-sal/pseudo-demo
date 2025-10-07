from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def modTwo(x: int) -> int:
            return x - ((x // 2) * 2)

        def zeroList(length: int) -> List[int]:
            return [0] * length

        parity = [modTwo(num) for num in nums]

        prefix_special = zeroList(len(nums))

        def computePrefix(k: int) -> None:
            if k == len(nums):
                return
            if parity[k] != parity[k - 1]:
                prefix_special[k] = prefix_special[k - 1]
            else:
                prefix_special[k] = prefix_special[k - 1] + 1
            computePrefix(k + 1)

        if len(nums) > 1:
            computePrefix(1)

        result: List[bool] = []

        def analyzeQueries(index: int) -> None:
            if index == len(queries):
                return
            start, end_ = queries[index]
            if start == end_:
                result.append(True)
            else:
                numerator = prefix_special[end_] - prefix_special[start] if start > 0 else prefix_special[end_]
                result.append(numerator == 0)
            analyzeQueries(index + 1)

        analyzeQueries(0)

        return result