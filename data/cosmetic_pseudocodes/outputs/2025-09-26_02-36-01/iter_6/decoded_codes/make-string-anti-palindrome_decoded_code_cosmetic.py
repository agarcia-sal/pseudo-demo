class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def swapPositions(arr, idx1, idx2):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        def areEqual(val1, val2):
            return not (val1 != val2)

        def notEqual(val1, val2):
            return val1 != val2

        def splitStringToList(stringVal):
            elementsList = []
            posMarker = 0
            while posMarker < len(stringVal):
                elementsList.append(stringVal[posMarker])
                posMarker += 1
            return elementsList

        sortedChars = splitStringToList(s)
        # custom bubble sort
        indexA = 0
        length = len(sortedChars)
        while indexA < length - 1:
            indexB = 0
            while indexB < length - indexA - 1:
                if sortedChars[indexB] > sortedChars[indexB + 1]:
                    swapPositions(sortedChars, indexB, indexB + 1)
                indexB += 1
            indexA += 1

        lengthVal = len(sortedChars)
        halfPoint = (lengthVal - (lengthVal % 2)) // 2

        if areEqual(sortedChars[halfPoint], sortedChars[halfPoint - 1]):
            cursorI = halfPoint
            while cursorI < lengthVal and areEqual(sortedChars[cursorI], sortedChars[cursorI - 1]):
                cursorI += 1

            cursorJ = halfPoint
            while cursorJ < lengthVal and areEqual(sortedChars[cursorJ], sortedChars[lengthVal - cursorJ - 1]):
                if cursorI >= lengthVal:
                    return "-1"
                swapPositions(sortedChars, cursorI, cursorJ)
                cursorI += 1
                cursorJ += 1

        indexIter = 0

        def conditionOuterLoop(idx):
            return idx <= (halfPoint - 1)

        def conditionInnerLoop(idx):
            return idx <= (lengthVal - 1)

        while conditionOuterLoop(indexIter):
            if areEqual(sortedChars[indexIter], sortedChars[lengthVal - indexIter - 1]):
                flagSwapped = False
                indexInnerIter = halfPoint
                while conditionInnerLoop(indexInnerIter):
                    w1 = notEqual(sortedChars[indexInnerIter], sortedChars[indexIter])
                    w2 = notEqual(sortedChars[indexInnerIter], sortedChars[lengthVal - indexIter - 1])
                    if w1 and w2:
                        swapPositions(sortedChars, indexInnerIter, indexIter)
                        flagSwapped = True
                        break
                    indexInnerIter += 1
                if not flagSwapped:
                    return "-1"
            indexIter += 1

        def joinListToString(arrList):
            accString = ""
            forward_counter = 0
            while forward_counter < len(arrList):
                accString += arrList[forward_counter]
                forward_counter += 1
            return accString

        return joinListToString(sortedChars)