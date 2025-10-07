class Solution:
    def maxScore(self, numbers):
        lengthVar = len(numbers)
        dpArray = [0] * lengthVar
        dpArray[0] = 0
        outerCounter = 1
        while outerCounter < lengthVar:
            innerCounter = 0
            while innerCounter < outerCounter:
                candidateValue = dpArray[innerCounter] + (outerCounter - innerCounter) * numbers[outerCounter]
                if dpArray[outerCounter] < candidateValue:
                    dpArray[outerCounter] = candidateValue
                innerCounter += 1
            outerCounter += 1
        return dpArray[lengthVar - 1]