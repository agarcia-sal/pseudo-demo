class Solution:
    def minimumOperations(self, nums, target):
        length = len(nums)
        result = abs(target[0] - nums[0])
        index = 1
        while index < length:
            diffCurrent = target[index] - nums[index]
            diffPrev = target[index - 1] - nums[index - 1]
            if diffCurrent * diffPrev > 0:
                diffAbsCurrent = abs(diffCurrent)
                diffAbsPrev = abs(diffPrev)
                delta = diffAbsCurrent - diffAbsPrev
                if delta > 0:
                    result += delta
            else:
                result += abs(diffCurrent)
            index += 1
        return result