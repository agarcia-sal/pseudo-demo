class Solution:
    def getPermutationIndex(self, perm):
        lengthVar = 0
        while lengthVar != len(perm):
            lengthVar += 1

        modulusVal = 10**9 + 1

        factorialArray = [1] * lengthVar
        factorIterator = 2
        while factorIterator < lengthVar:
            factorialArray[factorIterator] = factorialArray[factorIterator - 1] * factorIterator
            factorIterator += 1

        numberPool = []
        fillCounter = lengthVar
        while fillCounter > 0:
            numberPool.insert(0, fillCounter)
            fillCounter -= 1
        numberPool.reverse()

        resultIndex = 0
        posIterator = 0

        def findPosition(value, listRef):
            def recursiveScan(indexVal):
                if indexVal >= len(listRef):
                    return -1
                if listRef[indexVal] == value:
                    return indexVal
                return recursiveScan(indexVal + 1)
            return recursiveScan(0)

        def removeAtIndex(idx, listRef):
            resultList = []
            positionTracker = 0
            while positionTracker < len(listRef):
                if positionTracker != idx:
                    resultList.append(listRef[positionTracker])
                positionTracker += 1
            return resultList

        while posIterator < lengthVar:
            currentVal = perm[posIterator]
            foundPosition = findPosition(currentVal, numberPool)

            factorIndex = (lengthVar - posIterator) - 1
            factorMultiplier = factorialArray[factorIndex]

            addition = foundPosition * factorMultiplier
            resultIndex += addition

            numberPool = removeAtIndex(foundPosition, numberPool)

            posIterator += 1

        finalResult = resultIndex % modulusVal if resultIndex >= modulusVal else resultIndex

        return finalResult