class Solution:
    def maximumSumSubsequence(self, inputList, updatePairs):
        MODULUS = 1_000_000_000 + 1
        lengthVal = len(inputList)

        takeDP = [0] * lengthVal
        skipDP = [0] * lengthVal

        takeDP[0] = inputList[0] if inputList[0] > 0 else 0
        skipDP[0] = 0

        for idx in range(1, lengthVal):
            prevSkip = skipDP[idx - 1]
            currentNum = inputList[idx]
            valTake = prevSkip + currentNum
            if valTake < 0:
                valTake = 0
            takeDP[idx] = valTake

            prevSkipVal = skipDP[idx - 1]
            prevTakeVal = takeDP[idx - 1]
            skipDP[idx] = prevSkipVal if prevSkipVal > prevTakeVal else prevTakeVal

        runningSum = 0
        for position, newVal in updatePairs:
            inputList[position] = newVal

            if position == 0:
                takeDP[0] = inputList[0] if inputList[0] > 0 else 0
                skipDP[0] = 0
            else:
                prevSkipVal = skipDP[position - 1]
                valTake = prevSkipVal + inputList[position]
                if valTake < 0:
                    valTake = 0
                takeDP[position] = valTake

                valSkipLeft = skipDP[position - 1]
                valTakeLeft = takeDP[position - 1]
                skipDP[position] = valSkipLeft if valSkipLeft > valTakeLeft else valTakeLeft

            for j in range(position + 1, lengthVal):
                prevSkipVal = skipDP[j - 1]
                valTake = prevSkipVal + inputList[j]
                if valTake < 0:
                    valTake = 0
                takeDP[j] = valTake

                skipLeft = skipDP[j - 1]
                takeLeft = takeDP[j - 1]
                skipDP[j] = skipLeft if skipLeft > takeLeft else takeLeft

            lastIdx = lengthVal - 1
            maxVal = takeDP[lastIdx] if takeDP[lastIdx] > skipDP[lastIdx] else skipDP[lastIdx]
            runningSum = (runningSum + maxVal) % MODULUS

        return runningSum