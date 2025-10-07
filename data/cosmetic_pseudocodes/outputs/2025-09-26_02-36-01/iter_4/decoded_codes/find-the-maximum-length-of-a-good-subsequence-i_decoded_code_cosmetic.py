class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        lengthNums = len(nums)
        # Initialize dpMatrix with 1's: rows = lengthNums, cols = k+1
        dpMatrix = [[1] * (k + 1) for _ in range(lengthNums)]
        maxAnswer = 0

        for currentIndex in range(lengthNums):
            currentValue = nums[currentIndex]
            for hValue in range(k + 1):
                for previousIndex in range(currentIndex):
                    previousValue = nums[previousIndex]
                    if currentValue == previousValue:
                        candidate2 = dpMatrix[previousIndex][hValue] + 1
                        if candidate2 > dpMatrix[currentIndex][hValue]:
                            dpMatrix[currentIndex][hValue] = candidate2
                    else:
                        if hValue > 0:
                            candidateB = dpMatrix[previousIndex][hValue - 1] + 1
                            if candidateB > dpMatrix[currentIndex][hValue]:
                                dpMatrix[currentIndex][hValue] = candidateB
            if dpMatrix[currentIndex][k] > maxAnswer:
                maxAnswer = dpMatrix[currentIndex][k]

        return maxAnswer