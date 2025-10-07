from typing import List

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        lengthNums = len(nums)
        if lengthNums == 1:
            return nums[0]

        dpArr = [0] * lengthNums
        dpArr[lengthNums - 1] = nums[lengthNums - 1]

        idx = lengthNums - 2
        while idx >= 0:
            accumCost = nums[idx]
            if accumCost > dpArr[idx + 1]:
                dpArr[idx] = accumCost
            else:
                dpArr[idx] = dpArr[idx + 1] + accumCost

            pos = idx + 1
            while pos < lengthNums:
                signVal = 1
                diffVal = pos - idx
                if diffVal % 2 != 0:
                    signVal = -1

                accumCost += signVal * nums[pos]

                if (pos + 1) < lengthNums:
                    if dpArr[idx] < accumCost + dpArr[pos + 1]:
                        dpArr[idx] = accumCost + dpArr[pos + 1]
                else:
                    if dpArr[idx] < accumCost:
                        dpArr[idx] = accumCost
                pos += 1
            idx -= 1

        return dpArr[0]