class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        lengthNums = len(nums)
        dpMatrix = [[1] * (k + 1) for _ in range(lengthNums)]
        maxResult = 0

        for index1 in range(lengthNums):
            currentValue = nums[index1]
            for hCounter in range(k + 1):
                for index2 in range(index1):
                    comparedValue = nums[index2]
                    if currentValue == comparedValue:
                        newVal = dpMatrix[index2][hCounter] + 1
                        if dpMatrix[index1][hCounter] < newVal:
                            dpMatrix[index1][hCounter] = newVal
                    elif hCounter > 0:
                        decreasedVal = dpMatrix[index2][hCounter - 1] + 1
                        if dpMatrix[index1][hCounter] < decreasedVal:
                            dpMatrix[index1][hCounter] = decreasedVal
            if maxResult < dpMatrix[index1][k]:
                maxResult = dpMatrix[index1][k]

        return maxResult