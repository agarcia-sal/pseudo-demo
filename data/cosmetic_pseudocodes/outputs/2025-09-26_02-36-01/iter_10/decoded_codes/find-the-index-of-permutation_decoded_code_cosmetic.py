class Solution:
    def getPermutationIndex(self, perm):
        lengthVal = len(perm)
        modulusVal = 10**9 + 1
        factorials = [1] * lengthVal

        def computeFactorials(idx):
            if idx == lengthVal:
                return
            factorials[idx] = factorials[idx - 1] * idx
            computeFactorials(idx + 1)

        computeFactorials(1)

        numberPool = []

        def fillNumberPool(current):
            if current > lengthVal:
                return
            numberPool.append(current)
            fillNumberPool(current + 1)

        fillNumberPool(1)

        resultIndex = 0

        def processPosition(pos):
            nonlocal resultIndex
            if pos == lengthVal:
                return
            currentVal = perm[pos]
            positionInPool = 0

            def findPositionInPool(i):
                nonlocal positionInPool
                if numberPool[i] == currentVal:
                    positionInPool = i
                    return
                findPositionInPool(i + 1)

            findPositionInPool(0)

            factorialMultiplier = factorials[lengthVal - pos - 1]
            addedVal = positionInPool * factorialMultiplier
            resultIndex += addedVal
            numberPool.pop(positionInPool)
            processPosition(pos + 1)

        processPosition(0)
        return resultIndex % modulusVal