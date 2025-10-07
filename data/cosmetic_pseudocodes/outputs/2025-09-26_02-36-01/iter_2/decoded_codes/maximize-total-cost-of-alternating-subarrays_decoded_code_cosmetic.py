from typing import List

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        lengthVal = len(nums)
        if lengthVal == 1:
            return nums[0]

        dpList = [0] * lengthVal
        dpList[lengthVal - 1] = nums[lengthVal - 1]

        idx = lengthVal - 2
        while idx >= 0:
            tmpCost = nums[idx]

            if tmpCost > dpList[idx + 1]:
                dpList[idx] = tmpCost
            else:
                dpList[idx] = dpList[idx + 1] + tmpCost

            pos = idx + 1
            while pos < lengthVal:
                signFactor = 1 if ((pos - idx) % 2 == 0) else -1
                addition = nums[pos] * signFactor

                tmpCost += addition

                if (pos + 1) < lengthVal:
                    if dpList[idx] < tmpCost + dpList[pos + 1]:
                        dpList[idx] = tmpCost + dpList[pos + 1]
                else:
                    if dpList[idx] < tmpCost:
                        dpList[idx] = tmpCost
                pos += 1
            idx -= 1

        return dpList[0]