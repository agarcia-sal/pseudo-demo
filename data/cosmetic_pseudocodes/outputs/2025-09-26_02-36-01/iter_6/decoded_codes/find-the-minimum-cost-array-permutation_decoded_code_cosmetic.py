class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        full_mask = (1 << n) - 1
        memo = {}

        def computeDepth(bitmask, lastVal):
            if bitmask == full_mask:
                return abs(nums[lastVal] - nums[0])
            if (bitmask, lastVal) in memo:
                return memo[(bitmask, lastVal)]

            minimumDifference = float('inf')

            def recurseIndex(index):
                nonlocal minimumDifference
                if index > n - 1:
                    return
                isVisited = (bitmask >> index) & 1
                if isVisited == 0:
                    localCandidate = abs(nums[lastVal] - nums[index]) + computeDepth(bitmask | (1 << index), index)
                    if localCandidate < minimumDifference:
                        minimumDifference = localCandidate
                recurseIndex(index + 1)

            recurseIndex(0)
            memo[(bitmask, lastVal)] = minimumDifference
            return minimumDifference

        ans = []

        def generatePath(bitmask, lastSelected):
            ans.append(nums[lastSelected])
            if bitmask == full_mask:
                return
            targetValue = computeDepth(bitmask, lastSelected)
            currentIndex = n - 1
            while currentIndex >= 0:
                visitedFlag = (bitmask >> currentIndex) & 1
                if visitedFlag == 0:
                    evaluationValue = abs(nums[lastSelected] - nums[currentIndex]) + computeDepth(bitmask | (1 << currentIndex), currentIndex)
                    if evaluationValue == targetValue:
                        generatePath(bitmask | (1 << currentIndex), currentIndex)
                        break
                currentIndex -= 1

        generatePath(1 << 0, 0)
        return ans