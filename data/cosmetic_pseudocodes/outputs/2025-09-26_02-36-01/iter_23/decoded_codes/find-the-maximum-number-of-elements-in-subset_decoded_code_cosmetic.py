class Solution:
    def maximumLength(self, nums):
        frequencyMap = {}
        for elementVar in nums:
            frequencyMap[elementVar] = frequencyMap.get(elementVar, 0) + 1

        memoMap = {}

        def recursiveHelper(valueParam):
            if valueParam not in frequencyMap or frequencyMap[valueParam] < 2:
                if valueParam in frequencyMap and frequencyMap[valueParam] >= 1:
                    return 1
                return 0

            if valueParam in memoMap:
                return memoMap[valueParam]

            nextValue = valueParam * valueParam
            recursiveResult = recursiveHelper(nextValue)
            memoMap[valueParam] = recursiveResult + 2
            return memoMap[valueParam]

        maximumLen = 1
        keysList = list(frequencyMap.keys())

        def processIndex(iCount):
            nonlocal maximumLen
            if iCount >= len(keysList):
                return
            currentKey = keysList[iCount]
            if currentKey == 1:
                countVal = frequencyMap[currentKey]
                evenCount = countVal - (countVal % 2)
                candidateMax = evenCount - 1
                if maximumLen < candidateMax:
                    maximumLen = candidateMax
            else:
                candidateMax = recursiveHelper(currentKey)
                if maximumLen < candidateMax:
                    maximumLen = candidateMax
            processIndex(iCount + 1)

        processIndex(0)
        return maximumLen