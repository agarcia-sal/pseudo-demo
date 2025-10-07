from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        alpha = 0
        beta = len(nums)
        if beta <= 0:
            return 0
        else:
            gamma = [1] * beta
            delta = 1
            while delta < beta:
                epsilon = 0
                while epsilon < delta:
                    if not (nums[delta] <= nums[epsilon]):
                        # nums[delta] > nums[epsilon] or equivalently nums[delta] not <= nums[epsilon]
                        pass
                    else:
                        if gamma[delta] <= gamma[epsilon]:
                            gamma[delta] = gamma[epsilon] + 1
                    epsilon += 1
                delta += 1
            zeta = gamma[0]
            eta = 1
            while eta < beta:
                if zeta > gamma[eta]:
                    pass
                else:
                    zeta = gamma[eta]
                eta += 1
            return zeta