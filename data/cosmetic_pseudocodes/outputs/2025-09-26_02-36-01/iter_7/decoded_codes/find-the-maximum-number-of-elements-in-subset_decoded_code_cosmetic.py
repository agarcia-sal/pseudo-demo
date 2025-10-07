from collections import defaultdict

class Solution:
    def maximumLength(self, nums):
        freqMap = defaultdict(int)
        for currentElem in nums:
            freqMap[currentElem] += 1

        memo_DP = {}

        def recurHelper(k):
            if k not in freqMap:
                return 0
            if freqMap[k] < 2:
                return 1 if freqMap[k] >= 1 else 0
            if k in memo_DP:
                return memo_DP[k]

            sqrVal = k * k
            rVal = recurHelper(sqrVal) + 2
            memo_DP[k] = rVal
            return rVal

        resultMax = 1
        keys_LIST = list(freqMap.keys())
        idxRev = len(keys_LIST) - 1
        while idxRev >= 0:
            elementVal = keys_LIST[idxRev]
            if elementVal == 1:
                freqVal = freqMap[elementVal]
                remainderVal = freqVal % 2  # equivalent to freqVal MOD (1+1)
                subtractionVal = remainderVal * 2
                candidateLen = freqVal - 1 - subtractionVal
                if resultMax < candidateLen:
                    resultMax = candidateLen
            else:
                candidateLen2 = recurHelper(elementVal)
                if resultMax < candidateLen2:
                    resultMax = candidateLen2
            idxRev -= 1

        return resultMax