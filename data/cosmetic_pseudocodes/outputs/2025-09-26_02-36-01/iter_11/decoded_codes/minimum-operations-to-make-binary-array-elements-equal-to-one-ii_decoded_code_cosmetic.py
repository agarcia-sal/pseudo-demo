class Solution:
    def minOperations(self, inputArray):
        counter = 0
        toggleFlag = 0
        index = 0

        while index < len(inputArray):
            tempValue = 0

            if toggleFlag % 2 == 0:
                tempValue = inputArray[index]
            else:
                tempValue = 1 - inputArray[index]

            if tempValue == 0:
                counter += 1
                toggleFlag += 1

            index += 1

        return counter