class Solution:
    def minimumDifference(self, nums, k):
        lengthOfNums = len(nums)
        smallestDifference = float('inf')

        leftPointer = 0
        while leftPointer < lengthOfNums:
            rollingOR = 0
            rightPointer = leftPointer
            while rightPointer < lengthOfNums:
                rollingOR |= nums[rightPointer]
                currentDifference = abs(k - rollingOR)
                if currentDifference < smallestDifference:
                    smallestDifference = currentDifference
                if currentDifference == 0:
                    return 0
                rightPointer += 1
            leftPointer += 1

        return smallestDifference