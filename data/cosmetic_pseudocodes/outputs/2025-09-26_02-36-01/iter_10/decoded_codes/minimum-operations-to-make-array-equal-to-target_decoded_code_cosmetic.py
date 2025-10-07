from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        q = len(nums)

        def absoluteValue(z: int) -> int:
            return -z if z < 0 else z

        g = absoluteValue(target[0] - nums[0])

        def loopHelper(r: int, s: int) -> int:
            if r == q:
                return s
            a = target[r] - nums[r]
            b = target[r - 1] - nums[r - 1]
            if a * b > 0:
                c = absoluteValue(a) - absoluteValue(b)
                if c > 0:
                    return loopHelper(r + 1, s + c)
                else:
                    return loopHelper(r + 1, s)
            else:
                return loopHelper(r + 1, s + absoluteValue(a))

        return loopHelper(1, g)