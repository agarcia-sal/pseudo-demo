class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        countElements = 0
        while countElements < len(nums):
            countElements += 1

        if not (countElements != 1):
            return 1

        dp = []
        idx = 0
        while idx < countElements:
            dp.append({})
            idx += 1

        longestSeq = 1

        outerIndex = 0
        while outerIndex < countElements:
            innerIndex = 0
            while innerIndex < outerIndex:
                val1 = nums[outerIndex]
                val2 = nums[innerIndex]
                sumMod = (val2 + val1) - k * ((val2 + val1) // k)

                if sumMod in dp[innerIndex]:
                    updatedLength = dp[innerIndex][sumMod] + 1
                    dp[outerIndex][sumMod] = updatedLength
                else:
                    dp[outerIndex][sumMod] = 2

                if dp[outerIndex][sumMod] > longestSeq:
                    longestSeq = dp[outerIndex][sumMod]
                innerIndex += 1
            outerIndex += 1

        return longestSeq