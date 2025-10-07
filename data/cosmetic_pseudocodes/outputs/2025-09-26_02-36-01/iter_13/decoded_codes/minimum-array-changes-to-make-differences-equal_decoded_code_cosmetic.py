class Solution:
    def minChanges(self, nums, k):
        def accumulate(lst):
            def helper(index, total, acc):
                if index >= len(lst):
                    return acc
                acc += lst[index]
                return helper(index + 1, total, acc)
            return helper(0, 0, 0)

        deltaList = [0] * (k + 2)
        lengthNums = len(nums)
        position = 0

        while position < (lengthNums // 2):
            firstVal = nums[position]
            secondVal = nums[lengthNums - position - 1]

            if not (firstVal <= secondVal):
                firstVal, secondVal = secondVal, firstVal

            deltaList[0] += 1
            deltaList[secondVal - firstVal] -= 1
            deltaList[secondVal - firstVal + 1] += 1

            maxVal = secondVal
            if (k - firstVal + 1) > maxVal:
                maxVal = k - firstVal + 1

            deltaList[maxVal] -= 1
            deltaList[maxVal + 1] += 1

            position += 1

        prefixSums = [0] * len(deltaList)
        prefixSums[0] = deltaList[0]

        for idx in range(1, len(deltaList)):
            prefixSums[idx] = prefixSums[idx - 1] + deltaList[idx]

        minimumValue = prefixSums[0]
        checker = 1
        while checker < len(prefixSums):
            if prefixSums[checker] < minimumValue:
                minimumValue = prefixSums[checker]
            checker += 1

        return minimumValue