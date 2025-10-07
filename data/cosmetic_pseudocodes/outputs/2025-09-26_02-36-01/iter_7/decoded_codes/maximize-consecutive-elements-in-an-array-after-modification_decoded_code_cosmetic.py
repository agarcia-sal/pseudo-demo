class Solution:
    def maxSelectedElements(self, nums):
        result = 0
        memo = {}
        sortedNums = sorted(nums)

        for currentVal in sortedNums:
            valPlusOne = memo.get(currentVal + 1, 0)
            valMinusOne = memo.get(currentVal - 1, 0)

            memo[currentVal + 1] = valPlusOne + 1
            memo[currentVal] = valMinusOne + 1

            candidates = [result, memo[currentVal], memo[currentVal + 1]]
            maxCandidate = max(candidates)

            result = maxCandidate

        return result