from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        lengthNums = len(nums)
        delta = [0] * (k + 2)

        def accumulate(arr: List[int]) -> List[int]:
            total = 0
            accumulation = []
            for val in arr:
                total += val
                accumulation.append(total)
            return accumulation

        for index in range(lengthNums // 2):
            firstVal = nums[index]
            secondVal = nums[lengthNums - index - 1]
            if secondVal < firstVal:
                firstVal, secondVal = secondVal, firstVal

            delta[0] += 1
            delta[secondVal - firstVal] -= 1
            delta[secondVal - firstVal + 1] += 1

            maxVal = secondVal if secondVal >= (k - firstVal) else (k - firstVal)
            if maxVal + 1 < len(delta):
                delta[maxVal + 1] -= 1
            if maxVal + 2 < len(delta):
                delta[maxVal + 2] += 1

        prefixSum = accumulate(delta)
        return min(prefixSum)