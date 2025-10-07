class Solution:
    def countOfPairs(self, nums):
        BOUNDARY = 10**10 + 7
        lengthValue = len(nums)
        highestNumber = nums[0]
        for indexVar in range(1, lengthValue):
            if nums[indexVar] > highestNumber:
                highestNumber = nums[indexVar]

        def initialize3DArray(dim1, dim2, dim3):
            return [[[0] * dim3 for _ in range(dim2)] for __ in range(dim1)]

        dpArray = initialize3DArray(lengthValue, highestNumber + 1, highestNumber + 1)

        def assignInitialValues():
            stepVal = 0
            while True:
                if stepVal > nums[0]:
                    break
                complementaryVal = nums[0] - stepVal
                dpArray[0][stepVal][complementaryVal] = 1
                stepVal += 1

        assignInitialValues()

        def transferValues(currentIndex):
            if currentIndex >= lengthValue:
                return
            for firstLoopVar in range(nums[currentIndex] + 1):
                secondLoopVar = nums[currentIndex] - firstLoopVar
                for prevFirstLoopVar in range(firstLoopVar + 1):
                    for prevSecondLoopVar in range(secondLoopVar, highestNumber + 1):
                        prevValue = dpArray[currentIndex - 1][prevFirstLoopVar][prevSecondLoopVar]
                        currentValue = dpArray[currentIndex][firstLoopVar][secondLoopVar]
                        summedValue = currentValue + prevValue
                        dpArray[currentIndex][firstLoopVar][secondLoopVar] = summedValue % BOUNDARY
            transferValues(currentIndex + 1)

        transferValues(1)

        accumulatedResult = 0
        for outerCounter in range(highestNumber + 1):
            for innerCounter in range(highestNumber + 1):
                if (outerCounter + innerCounter) == nums[lengthValue - 1]:
                    accumulatedResult += dpArray[lengthValue - 1][outerCounter][innerCounter]
                    accumulatedResult %= BOUNDARY

        return accumulatedResult