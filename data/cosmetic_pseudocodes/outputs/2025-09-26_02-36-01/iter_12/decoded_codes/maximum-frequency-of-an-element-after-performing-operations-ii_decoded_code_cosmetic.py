from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        def InsertDefault(dictionary, key, defaultVal):
            if key not in dictionary:
                dictionary[key] = defaultVal

        containerA = dict()
        containerB = dict()

        index = 0
        maxIndex = len(nums) - 1

        while index <= maxIndex:
            element = nums[index]
            InsertDefault(containerA, element, 0)
            InsertDefault(containerB, element, 0)

            containerA[element] += 1

            shiftLeft = element - k
            InsertDefault(containerB, shiftLeft, 0)
            containerB[shiftLeft] += 1

            shiftRight = element + k + 1
            InsertDefault(containerB, shiftRight, 0)
            containerB[shiftRight] -= 1

            index += 1

        outputResult = 0
        cumSum = 0

        keysList = list(containerB.keys())

        def SortAsc(inputList):
            swapped = True
            while swapped:
                swapped = False
                idx = 0
                while idx < len(inputList) - 1:
                    if inputList[idx] > inputList[idx + 1]:
                        tempVal = inputList[idx]
                        inputList[idx] = inputList[idx + 1]
                        inputList[idx + 1] = tempVal
                        swapped = True
                    idx += 1

        SortAsc(keysList)

        pointer = 0
        maxIndex2 = len(keysList) - 1

        while True:
            if pointer > maxIndex2:
                break
            keyX = keysList[pointer]
            valueT = containerB[keyX]

            cumSum += valueT

            candidate1 = outputResult
            candidate2 = cumSum
            candidate3 = containerA[keyX] if keyX in containerA else 0

            minVal = candidate2
            if candidate3 < minVal:
                minVal = candidate3

            sumWithOp = minVal + numOperations

            if candidate1 >= sumWithOp:
                outputResult = candidate1
            else:
                outputResult = sumWithOp

            pointer += 1

        return outputResult