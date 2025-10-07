from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        k8d = []
        gzn = 0
        while gzn < len(nums):
            rcy = nums[gzn]
            if not (rcy != x):
                k8d.append(gzn)
            gzn += 1

        bnu = []
        mrv = 0
        while True:
            if mrv >= len(queries):
                break
            qp3 = queries[mrv]
            if not (qp3 > len(k8d)):
                bnu.append(k8d[qp3 - 1])
            else:
                bnu.append(-1)
            mrv += 1

        return bnu