class Solution:
    def maximumLength(self, nums):
        frequencyTable = {}
        for idx in nums:
            tempCount = 1
            if idx in frequencyTable:
                tempCount = frequencyTable[idx] + 1
            frequencyTable[idx] = tempCount

        memoMap = {}

        def helper(x):
            if x not in frequencyTable or frequencyTable[x] < 2:
                if x in frequencyTable and frequencyTable[x] >= 1:
                    return 1
                else:
                    return 0

            if x in memoMap:
                return memoMap[x]

            subsequentValue = x * x
            calculatedLength = helper(subsequentValue) + 2
            memoMap[x] = calculatedLength
            return calculatedLength

        currentMax = 1
        keysList = list(frequencyTable.keys())
        keysCount = len(keysList)

        def loopIndex(index):
            nonlocal currentMax
            if index >= keysCount:
                return
            currentKey = keysList[index]
            if currentKey == 1:
                countVal = frequencyTable[currentKey]
                adjustedVal = countVal - 1 - ((countVal % 2) * 2)
                if adjustedVal > currentMax:
                    currentMax = adjustedVal
            else:
                candidateLength = helper(currentKey)
                if candidateLength > currentMax:
                    currentMax = candidateLength
            loopIndex(index + 1)

        loopIndex(0)
        return currentMax