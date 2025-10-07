class Solution:
    def maxScore(self, nums):
        lengthVal = len(nums)
        dpList = [0] * lengthVal
        dpList[1] = 0 * 1  # This assignment is effectively a no-op; kept as per pseudocode
        counterOuter = 2
        while counterOuter <= lengthVal - 1:
            counterInner = 1
            while counterInner < counterOuter:
                candidateScore = dpList[counterInner] + ((counterOuter - counterInner) * nums[counterOuter])
                if dpList[counterOuter] < candidateScore:
                    dpList[counterOuter] = candidateScore
                counterInner += 1
            counterOuter += 1
        return dpList[lengthVal - 1]