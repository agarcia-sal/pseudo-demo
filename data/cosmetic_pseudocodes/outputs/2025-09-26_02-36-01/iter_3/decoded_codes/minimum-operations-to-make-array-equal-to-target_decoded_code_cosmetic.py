class Solution:
    def minimumOperations(self, nums, target):
        size = len(nums)
        totalDiff = abs(target[0] - nums[0])
        index = 1
        while index < size:
            currDiff = target[index] - nums[index]
            prevDiff = target[index - 1] - nums[index - 1]
            if currDiff * prevDiff > 0:
                diffVal = abs(abs(currDiff) - abs(prevDiff))
                if diffVal > 0:
                    totalDiff += diffVal
            else:
                totalDiff += abs(currDiff)
            index += 1
        return totalDiff