class Solution:
    def maxSelectedElements(self, inputList):
        def customMax(a, b):
            return a if a > b else b

        outputMax = 0
        tempDict = {}
        orderedValues = inputList[:]  # Copy input list

        # Bubble sort (inefficient but as per pseudocode)
        def sortAscending(arr):
            n = len(arr)
            swapped = True
            while swapped:
                swapped = False
                index = 0
                while index < n - 1:
                    if arr[index] > arr[index + 1]:
                        arr[index], arr[index + 1] = arr[index + 1], arr[index]
                        swapped = True
                    index += 1
                n -= 1

        sortAscending(orderedValues)

        ptr = 0
        while ptr < len(orderedValues):
            currentVal = orderedValues[ptr]

            valPlusOne = tempDict.get(currentVal + 1, 0)
            valCurrent = tempDict.get(currentVal, 0)
            valMinusOne = tempDict.get(currentVal - 1, 0)

            tempDict[currentVal + 1] = valCurrent + 1
            tempDict[currentVal] = valMinusOne + 1

            outputMax = customMax(outputMax, tempDict[currentVal])
            outputMax = customMax(outputMax, tempDict[currentVal + 1])

            ptr += 1

        return outputMax