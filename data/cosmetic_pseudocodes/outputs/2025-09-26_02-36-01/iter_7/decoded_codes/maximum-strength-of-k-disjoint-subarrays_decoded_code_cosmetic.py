class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        totalElements = len(nums)
        NEG_INF = -10**9
        memoizationGrid = [[NEG_INF] * (k + 1) for _ in range(totalElements + 1)]
        memoizationGrid[0][0] = 0

        for outerIndex in range(1, totalElements + 1):
            for innerCount in range(1, k + 1):
                accumulator = 0
                reverseIndex = outerIndex
                while reverseIndex >= 1:
                    accumulator += nums[reverseIndex - 1]
                    if (innerCount % 2) == 1:
                        polarityFactor = (k - innerCount)
                    else:
                        polarityFactor = - (k - innerCount)
                    potentialValue = memoizationGrid[reverseIndex - 1][innerCount - 1] + polarityFactor * accumulator
                    if potentialValue > memoizationGrid[outerIndex][innerCount]:
                        memoizationGrid[outerIndex][innerCount] = potentialValue
                    reverseIndex -= 1

                previousValue = memoizationGrid[outerIndex - 1][innerCount]
                if previousValue > memoizationGrid[outerIndex][innerCount]:
                    memoizationGrid[outerIndex][innerCount] = previousValue

        return memoizationGrid[totalElements][k]