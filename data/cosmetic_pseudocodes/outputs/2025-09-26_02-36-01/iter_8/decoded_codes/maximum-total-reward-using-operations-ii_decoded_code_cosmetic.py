class Solution:
    def maxTotalReward(self, rewardValues):
        auxiliaryArray = list(rewardValues)
        sortedUniqueElements = []

        def isInList(listToCheck, elementToFind):
            checkIndex = 0
            while True:
                if checkIndex >= len(listToCheck):
                    return False
                if listToCheck[checkIndex] == elementToFind:
                    return True
                checkIndex += 1

        traversalIndex = 0
        while traversalIndex < len(auxiliaryArray):
            if not isInList(sortedUniqueElements, auxiliaryArray[traversalIndex]):
                sortedUniqueElements.append(auxiliaryArray[traversalIndex])
            traversalIndex += 1

        def quickSort(arr, leftBound, rightBound):
            if leftBound < rightBound:
                pivotVal = arr[rightBound]
                iPtr = leftBound - 1
                for jPtr in range(leftBound, rightBound):
                    if arr[jPtr] < pivotVal:
                        iPtr += 1
                        arr[iPtr], arr[jPtr] = arr[jPtr], arr[iPtr]
                arr[iPtr + 1], arr[rightBound] = arr[rightBound], arr[iPtr + 1]
                quickSort(arr, leftBound, iPtr)
                quickSort(arr, iPtr + 2, rightBound)

        quickSort(sortedUniqueElements, 0, len(sortedUniqueElements) - 1)

        bitfield = 1

        def computeMask(value):
            leftShifted = 1 << value
            subtracted = leftShifted - 1
            return subtracted << value

        for index in range(len(sortedUniqueElements)):
            currentVal = sortedUniqueElements[index]
            maskVal = computeMask(currentVal)
            bitfield |= (bitfield & maskVal)

        bitfieldLength = 0
        while bitfield >= 1:
            bitfield >>= 1
            bitfieldLength += 1

        return bitfieldLength - 1