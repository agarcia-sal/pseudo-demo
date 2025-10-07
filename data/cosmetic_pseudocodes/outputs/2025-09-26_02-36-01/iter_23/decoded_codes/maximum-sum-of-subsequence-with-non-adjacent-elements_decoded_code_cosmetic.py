class Solution:
    def maximumSumSubsequence(self, nums, queries):
        modValue = 10 ** 9 + 1
        lengthVal = len(nums)

        def computeStep(aryTake, arySkip, valArr, idx):
            if idx < 0:
                return
            prevSkip = arySkip[idx - 1] if idx - 1 >= 0 else 0
            prevTake = aryTake[idx - 1] if idx - 1 >= 0 else 0

            currentTake = (prevSkip if prevSkip > 0 else 0) + valArr[idx]
            if currentTake < 0:
                currentTake = 0

            currentSkip = prevSkip if prevSkip > prevTake else prevTake

            aryTake[idx] = currentTake
            arySkip[idx] = currentSkip

        def recalcRange(aryTake, arySkip, valArr, startIdx, endIdx):
            i = startIdx
            while i < endIdx:
                computeStep(aryTake, arySkip, valArr, i)
                i += 1

        arrTake = [0] * lengthVal
        arrSkip = [0] * lengthVal

        arrTake[0] = nums[0] if nums[0] > 0 else 0
        arrSkip[0] = 0

        recalcRange(arrTake, arrSkip, nums, 1, lengthVal)

        def maxOfTwo(a, b):
            return a if a > b else b

        resultSum = 0

        for position, newVal in queries:
            nums[position] = newVal

            if position == 0:
                arrTake[0] = nums[0] if nums[0] > 0 else 0
                arrSkip[0] = 0
            else:
                computeStep(arrTake, arrSkip, nums, position)

            recalcRange(arrTake, arrSkip, nums, position + 1, lengthVal)

            maxEndVal = maxOfTwo(arrTake[lengthVal - 1], arrSkip[lengthVal - 1])
            resultSum = (resultSum + maxEndVal) % modValue

        return resultSum