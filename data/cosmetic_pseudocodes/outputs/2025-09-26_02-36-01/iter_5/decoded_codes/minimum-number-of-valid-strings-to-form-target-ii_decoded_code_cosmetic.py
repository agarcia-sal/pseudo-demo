class Solution:
    def minValidStrings(self, words, target):
        def constructPrefixes(index1, index2, currentWord, accumulated):
            if index2 > len(currentWord):
                return accumulated
            newPrefix = accumulated | {currentWord[index1:index2]}
            return constructPrefixes(index1, index2 + 1, currentWord, newPrefix)

        def buildAllPrefixes(listWords, idx, accumulatedSet):
            if idx >= len(listWords):
                return accumulatedSet
            updatedSet = constructPrefixes(0, 1, listWords[idx], accumulatedSet)
            return buildAllPrefixes(listWords, idx + 1, updatedSet)

        allPrefixes = buildAllPrefixes(words, 0, set())
        lenTarget = len(target)
        INF = 10 * (lenTarget + 1)

        dpArray = [INF] * (lenTarget + 1)
        dpArray[0] = 0

        def findMin(indexOuter):
            if indexOuter > lenTarget:
                return

            def checkPrefixes(indexInner):
                if indexInner > indexOuter:
                    return
                candidateSubstr = target[indexInner - 1:indexOuter]
                if candidateSubstr in allPrefixes:
                    prevVal = dpArray[indexInner - 1]
                    dpArray[indexOuter] = min(dpArray[indexOuter], prevVal + 1)
                checkPrefixes(indexInner + 1)

            checkPrefixes(1)
            findMin(indexOuter + 1)

        findMin(1)

        resultValue = dpArray[lenTarget]
        negativeOne = -1

        if resultValue != INF:
            return resultValue
        else:
            return negativeOne