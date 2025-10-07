class Solution:
    def getPermutationIndex(self, perm):
        lengthCount = len(perm)
        modulusValue = 10 ** 10

        factorials = [1] * lengthCount
        iteratorVar = 2
        while iteratorVar <= lengthCount - 1:
            prevFact = factorials[iteratorVar - 1]
            updatedFact = prevFact * iteratorVar
            factorials[iteratorVar] = updatedFact
            iteratorVar += 1

        availableNums = list(range(1, lengthCount + 1))

        resultIndex = 0
        idxCounter = 0
        while idxCounter < lengthCount:
            currentVal = perm[idxCounter]
            searchIndex = 0
            foundFlag = False

            while not foundFlag and searchIndex < len(availableNums):
                if availableNums[searchIndex] == currentVal:
                    posIndex = searchIndex
                    foundFlag = True
                else:
                    searchIndex += 1

            factIndex = lengthCount - idxCounter - 1
            multipliedVal = posIndex * factorials[factIndex]

            resultIndex += multipliedVal

            leftPart = availableNums[0:posIndex]
            rightPart = availableNums[posIndex + 1:]
            availableNums = leftPart + rightPart

            idxCounter += 1

        finalResult = resultIndex % modulusValue
        return finalResult