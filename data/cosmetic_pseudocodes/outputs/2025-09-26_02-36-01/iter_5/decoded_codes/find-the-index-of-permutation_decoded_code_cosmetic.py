class Solution:
    def getPermutationIndex(self, perm):
        lengthVal = len(perm)
        modulusVal = 10**9 + 1

        factorialArray = [1] * lengthVal
        for i in range(1, lengthVal):
            factorialArray[i] = factorialArray[i - 1] * i

        availableNums = list(range(1, lengthVal + 1))

        resultIndex = 0

        def processPosition(idx):
            nonlocal resultIndex
            if idx >= lengthVal:
                return

            currentVal = perm[idx]

            positionInList = 0
            while positionInList < len(availableNums):
                if availableNums[positionInList] == currentVal:
                    break
                positionInList += 1

            decrementFactorPosition = lengthVal - idx - 1
            additionValue = positionInList * factorialArray[decrementFactorPosition]
            resultIndex += additionValue

            availableNums.pop(positionInList)

            processPosition(idx + 1)

        processPosition(0)

        finalResult = resultIndex % modulusVal
        return finalResult