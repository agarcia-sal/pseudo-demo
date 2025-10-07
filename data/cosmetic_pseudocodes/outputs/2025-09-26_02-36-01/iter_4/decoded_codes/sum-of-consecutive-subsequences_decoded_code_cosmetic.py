from collections import Counter

class Solution:
    def getSum(self, nums):
        MOD = 10**9 + 7

        def calc(nums):
            length = len(nums)
            leftCounts = [0] * length
            rightCounts = [0] * length

            frequencyMap = Counter()
            for index in range(1, length):
                keyLeft = nums[index - 1]
                previousCountLeft = frequencyMap[keyLeft]
                frequencyMap[keyLeft] = previousCountLeft + 1
                leftCounts[index] = previousCountLeft

            frequencyMap = Counter()
            for index in range(length - 2, -1, -1):
                keyRight = nums[index + 1]
                previousCountRight = frequencyMap[keyRight]
                frequencyMap[keyRight] = previousCountRight + 1
                rightCounts[index] = previousCountRight

            accumulatedSum = 0
            for pos in range(length):
                l = leftCounts[pos]
                r = rightCounts[pos]
                val = nums[pos]

                partialSum = (l + r + (l * r)) * val
                accumulatedSum += partialSum

            return accumulatedSum % MOD

        xResult = calc(nums)

        leftIndex, rightIndex = 0, len(nums) - 1
        while leftIndex < rightIndex:
            nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
            leftIndex += 1
            rightIndex -= 1

        yResult = calc(nums)

        sumNums = sum(nums)

        return (xResult + yResult + sumNums) % MOD