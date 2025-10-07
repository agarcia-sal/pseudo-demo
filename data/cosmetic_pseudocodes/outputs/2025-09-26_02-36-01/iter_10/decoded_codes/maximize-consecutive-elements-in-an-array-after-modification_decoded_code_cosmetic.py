class Solution:
    def maxSelectedElements(self, nums):
        maxCount = 0
        memo = {}
        sortedList = sorted(nums)

        def processNext(index):
            nonlocal maxCount
            if index > len(sortedList):
                return
            currentVal = sortedList[index - 1]
            valPlusOne = memo.get(currentVal + 1, 0)
            memo[currentVal + 1] = valPlusOne + 1
            valMinusOne = memo.get(currentVal - 1, 0)
            memo[currentVal] = valMinusOne + 1
            maxCount = max(maxCount, memo[currentVal + 1], memo[currentVal])
            processNext(index + 1)

        processNext(1)
        return maxCount