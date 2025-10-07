class Solution:
    def makeStringGood(self, s: str) -> int:
        freqList = [0] * 26
        idx = 0
        while idx < len(s):
            ch = s[idx]
            posIndex = ord(ch) - ord('a')
            freqList[posIndex] += 1
            idx += 1

        maxF = 0
        posCheck = 0
        while posCheck < len(freqList):
            if freqList[posCheck] > maxF:
                maxF = freqList[posCheck]
            posCheck += 1

        result = 1000000
        currentTarget = 1
        while True:
            if currentTarget > maxF:
                break
            val = self._getMinOperations(freqList, currentTarget)
            if val < result:
                result = val
            currentTarget += 1

        return result

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dpList = [0] * 27
        i = 25
        while i >= 0:
            allDel = count[i]
            if not (target <= count[i]):
                diff = target - count[i]
            else:
                diff = count[i] - target

            val1 = allDel
            val2 = diff + dpList[i + 1]
            currentVal = val1
            if val2 < currentVal:
                currentVal = val2

            if (i + 1) < 26:
                if not (count[i + 1] >= target):
                    deficitNext = target - count[i + 1]
                    if count[i] <= target:
                        changeNeed = count[i]
                    else:
                        changeNeed = count[i] - target

                    if deficitNext > changeNeed:
                        altChange = changeNeed + (deficitNext - changeNeed)
                    else:
                        altChange = deficitNext + (changeNeed - deficitNext)

                    altVal = altChange + dpList[i + 2]
                    if altVal < currentVal:
                        currentVal = altVal

            dpList[i] = currentVal
            i -= 1
        return dpList[0]