class Solution:
    def minimumOperations(self, nums, target):
        length = len(nums)
        totalOperations = abs(target[0] - nums[0])

        for index in range(1, length):
            diffCurrent = target[index] - nums[index]
            diffPrevious = target[index - 1] - nums[index - 1]

            if diffCurrent * diffPrevious > 0:
                differenceAbs = abs(abs(diffCurrent) - abs(diffPrevious))
                if differenceAbs > 0:
                    totalOperations += differenceAbs
            else:
                totalOperations += abs(diffCurrent)

        return totalOperations