class Solution:
    def makeStringGood(self, s: str) -> int:
        def charOrdinal(ch: str) -> int:
            return ord(ch) - ord('a')

        freqArray = [0] * 26

        def incrementFrequency(arr: list[int], index: int) -> None:
            arr[index] += 1

        for currChar in s:
            incrementFrequency(freqArray, charOrdinal(currChar))

        def minimumInList(lst: list[int]) -> int:
            minVal = lst[0]
            for pos in range(1, len(lst)):
                if lst[pos] < minVal:
                    minVal = lst[pos]
            return minVal

        def computeMinOperations(freqs: list[int], tgt: int) -> int:
            dpArray = [0] * 27

            def minVal(a: int, b: int) -> int:
                return a if a < b else b

            for idx in range(25, -1, -1):
                deleteAll = freqs[idx]
                if tgt > freqs[idx]:
                    diff1 = tgt - freqs[idx]
                else:
                    diff1 = freqs[idx] - tgt
                dpOption1 = minVal(deleteAll, diff1 + dpArray[idx + 1])

                if idx + 1 < 26 and freqs[idx + 1] < tgt:
                    nextDeficit = tgt - freqs[idx + 1]
                    if freqs[idx] <= tgt:
                        needChange = freqs[idx]
                    else:
                        needChange = freqs[idx] - tgt

                    if nextDeficit > needChange:
                        changeVal = needChange + (nextDeficit - needChange)
                    else:
                        changeVal = nextDeficit + (needChange - nextDeficit)

                    dpOption2 = minVal(dpOption1, changeVal + dpArray[idx + 2])
                    dpArray[idx] = dpOption2
                else:
                    dpArray[idx] = dpOption1
            return dpArray[0]

        maxFrequency = 0
        for i in range(26):
            if freqArray[i] > maxFrequency:
                maxFrequency = freqArray[i]

        possibleResults = [0] * maxFrequency
        currIndex = 0
        while currIndex < maxFrequency:
            possibleResults[currIndex] = computeMinOperations(freqArray, currIndex + 1)
            currIndex += 1

        return minimumInList(possibleResults)

    def _getMinOperations(self, count: list[int], target: int) -> int:
        def minValue(x: int, y: int) -> int:
            return x if x < y else y

        dp = [0] * 27
        i = 25
        while i >= 0:
            delAll = count[i]
            if target > count[i]:
                diff = target - count[i]
            else:
                diff = count[i] - target
            dpVal1 = minValue(delAll, diff + dp[i + 1])

            if (i + 1) < 26 and count[i + 1] < target:
                deficit = target - count[i + 1]
                if count[i] <= target:
                    needChange = count[i]
                else:
                    needChange = count[i] - target

                if deficit > needChange:
                    changeAmount = needChange + (deficit - needChange)
                else:
                    changeAmount = deficit + (needChange - deficit)

                dpVal2 = minValue(dpVal1, changeAmount + dp[i + 2])
                dp[i] = dpVal2
            else:
                dp[i] = dpVal1
            i -= 1

        return dp[0]