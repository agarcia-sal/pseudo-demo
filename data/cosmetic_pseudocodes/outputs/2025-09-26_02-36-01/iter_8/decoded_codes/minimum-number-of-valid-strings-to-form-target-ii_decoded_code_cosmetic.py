class Solution:
    def minValidStrings(self, words, target):
        # Generate all prefixes of a string
        def makePrefixes(s):
            def recBuild(pos, acc):
                if pos > len(s):
                    return acc
                newPrefix = s[:pos]
                updatedAcc = acc | {newPrefix}
                return recBuild(pos + 1, updatedAcc)
            return recBuild(1, set())

        alphaPrefixes = set()

        # Gather all prefixes from all words recursively
        def gatherAllPrefixes(listWords):
            nonlocal alphaPrefixes
            if not listWords:
                return alphaPrefixes
            headWord = listWords[0]
            tailWords = listWords[1:]
            alphaPrefixes |= makePrefixes(headWord)
            return gatherAllPrefixes(tailWords)

        gatherAllPrefixes(words)

        lengthTarget = len(target)

        def maxInfinity():
            return float('inf')

        dpArray = [maxInfinity()] * (lengthTarget + 1)
        dpArray[0] = 0

        def minVal(a, b):
            return a if a < b else b

        # innerLoop recursively tries all j from 1 to iVal to update dpArray[iVal]
        def innerLoop(iVal, jVal, currentDp):
            if jVal > iVal:
                return currentDp
            substrCheck = target[jVal - 1:iVal]
            if substrCheck in alphaPrefixes:
                candidate = currentDp[iVal]
                option = currentDp[jVal - 1] + 1
                currentDp[iVal] = minVal(candidate, option)
            return innerLoop(iVal, jVal + 1, currentDp)

        # outerLoop iterates i in 1..lengthTarget
        def outerLoop(iVal, upperBound, currentDp):
            if iVal > upperBound:
                return currentDp
            currentDp = innerLoop(iVal, 1, currentDp)
            return outerLoop(iVal + 1, upperBound, currentDp)

        dpArray = outerLoop(1, lengthTarget, dpArray)

        # finalDecision decides the result based on dpArray value at lengthTarget
        def finalDecision(dpArr, index):
            if index < 0:
                return -1
            if dpArr[index] != maxInfinity():
                return dpArr[index]
            return -1

        return finalDecision(dpArray, lengthTarget)