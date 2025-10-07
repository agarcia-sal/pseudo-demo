class Solution:
    def makeStringGood(self, s: str) -> int:
        freqList = [0] * 26
        maxFreq = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            freqList[idx] += 1
            if freqList[idx] > maxFreq:
                maxFreq = freqList[idx]

        minOps = -1
        for tmpTarget in range(1, maxFreq + 1):
            currentCount = self._getMinOperations(freqList, tmpTarget)
            if minOps < 0 or currentCount < minOps:
                minOps = currentCount
        return minOps

    def _getMinOperations(self, count: list[int], target: int) -> int:
        resultDp = [0] * 27  # size 27 to handle pos+2 indexing safely
        pos = 25
        while pos >= 0:
            delAll = count[pos]
            if target > count[pos]:
                toTarget = target - count[pos]
            else:
                toTarget = count[pos] - target

            dpVal = min(delAll, toTarget + resultDp[pos + 1])

            if (pos + 1) < 26 and count[pos + 1] < target:
                nextDeficit = target - count[pos + 1]
                if count[pos] <= target:
                    neededChanges = count[pos]
                else:
                    neededChanges = count[pos] - target

                if nextDeficit > neededChanges:
                    changeVal = neededChanges + (nextDeficit - neededChanges)
                else:
                    changeVal = nextDeficit + (neededChanges - nextDeficit)

                dpVal = min(dpVal, changeVal + resultDp[pos + 2])

            resultDp[pos] = dpVal
            pos -= 1

        return resultDp[0]