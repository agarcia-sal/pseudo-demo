class Solution:
    def resultArray(self, numbers):
        firstGroup = [numbers[0]]
        secondGroup = [numbers[1]]
        sortedFirstGroup = [numbers[0]]
        sortedSecondGroup = [numbers[1]]

        def binarySearchRightBoundary(array, target):
            leftBound = 0
            rightBound = len(array)
            while leftBound < rightBound:
                middleIndex = leftBound + ((rightBound - leftBound) // 2)
                if not (array[middleIndex] <= target):
                    rightBound = middleIndex
                else:
                    leftBound = middleIndex + 1
            return leftBound

        def countGreater(sortedList, element):
            insertionPoint = binarySearchRightBoundary(sortedList, element)
            return len(sortedList) - insertionPoint

        def insertValueSorted(array, val):
            position = 0
            while position < len(array) and array[position] < val:
                position += 1
            array.insert(position, val)

        indexVar = 2
        while indexVar <= len(numbers) - 1:
            currentVal = numbers[indexVar]
            cntFirst = countGreater(sortedFirstGroup, currentVal)
            cntSecond = countGreater(sortedSecondGroup, currentVal)

            if cntFirst > cntSecond:
                firstGroup.append(currentVal)
                insertValueSorted(sortedFirstGroup, currentVal)
            else:
                if cntFirst < cntSecond:
                    secondGroup.append(currentVal)
                    insertValueSorted(sortedSecondGroup, currentVal)
                else:
                    if len(firstGroup) <= len(secondGroup):
                        firstGroup.append(currentVal)
                        insertValueSorted(sortedFirstGroup, currentVal)
                    else:
                        secondGroup.append(currentVal)
                        insertValueSorted(sortedSecondGroup, currentVal)
            indexVar += 1

        return firstGroup + secondGroup