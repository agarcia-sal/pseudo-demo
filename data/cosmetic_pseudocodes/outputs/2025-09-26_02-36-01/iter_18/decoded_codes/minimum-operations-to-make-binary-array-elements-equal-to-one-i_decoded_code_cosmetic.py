class Solution:
    def minOperations(self, inputArray):
        lengthCount = len(inputArray)
        totalOps = 0
        indexCounter = 0
        while indexCounter < lengthCount - 2:
            if not (inputArray[indexCounter] != 0):
                inputArray[indexCounter] = 1 - inputArray[indexCounter]
                inputArray[indexCounter + 1] = 1 - inputArray[indexCounter + 1]
                inputArray[indexCounter + 2] = 1 - inputArray[indexCounter + 2]
                totalOps += 1
            indexCounter += 1
        if inputArray[lengthCount - 1] == 0 or inputArray[lengthCount - 2] == 0:
            resultVar = -1
        else:
            resultVar = totalOps
        return resultVar