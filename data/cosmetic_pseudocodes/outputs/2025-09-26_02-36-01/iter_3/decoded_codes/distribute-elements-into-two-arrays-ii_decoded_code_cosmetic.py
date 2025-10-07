class Solution:
    def resultArray(self, nums):
        if len(nums) < 2:
            return nums[:]  # Return a copy if less than 2 elements

        firstPart = [nums[0]]
        secondPart = [nums[1]]
        orderedFirst = [nums[0]]
        orderedSecond = [nums[1]]

        def greaterCount(arr, element):
            lowBound = 0
            highBound = len(arr)
            while lowBound < highBound:
                midPoint = lowBound + (highBound - lowBound) // 2
                if not (element < arr[midPoint]):
                    lowBound = midPoint + 1
                else:
                    highBound = midPoint
            return len(arr) - lowBound

        index = 2
        n = len(nums)
        while index < n:
            currentVal = nums[index]
            countFirst = greaterCount(orderedFirst, currentVal)
            countSecond = greaterCount(orderedSecond, currentVal)

            if countFirst > countSecond:
                firstPart.append(currentVal)
                insertPos = 0
                while insertPos < len(orderedFirst) and orderedFirst[insertPos] < currentVal:
                    insertPos += 1
                orderedFirst = orderedFirst[:insertPos] + [currentVal] + orderedFirst[insertPos:]
            elif countFirst < countSecond:
                secondPart.append(currentVal)
                insertPos2 = 0
                while insertPos2 < len(orderedSecond) and orderedSecond[insertPos2] < currentVal:
                    insertPos2 += 1
                orderedSecond = orderedSecond[:insertPos2] + [currentVal] + orderedSecond[insertPos2:]
            else:
                lenFirst = len(firstPart)
                lenSecond = len(secondPart)
                if lenFirst <= lenSecond:
                    firstPart.append(currentVal)
                    pos3 = 0
                    while pos3 < len(orderedFirst) and orderedFirst[pos3] < currentVal:
                        pos3 += 1
                    orderedFirst = orderedFirst[:pos3] + [currentVal] + orderedFirst[pos3:]
                else:
                    secondPart.append(currentVal)
                    pos4 = 0
                    while pos4 < len(orderedSecond) and orderedSecond[pos4] < currentVal:
                        pos4 += 1
                    orderedSecond = orderedSecond[:pos4] + [currentVal] + orderedSecond[pos4:]
            index += 1

        combinedResult = []
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(firstPart):
            combinedResult.append(firstPart[pointer1])
            pointer1 += 1
        while pointer2 < len(secondPart):
            combinedResult.append(secondPart[pointer2])
            pointer2 += 1

        return combinedResult