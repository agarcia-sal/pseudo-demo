class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = [0] * 26
        idx = 0
        while idx < len(s):
            ch = s[idx]
            pos = ord(ch) - ord('a')
            freq[pos] += 1
            idx += 1

        maxCount = 0
        j = 0
        while j < 26:
            if freq[j] > maxCount:
                maxCount = freq[j]
            j += 1

        opsList = []
        tar = 1
        while tar <= maxCount:
            opsList.append(self._getMinOperations(freq, tar))
            tar += 1

        result = opsList[0]
        k = 1
        while k < len(opsList):
            if opsList[k] < result:
                result = opsList[k]
            k += 1

        return result

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dpArr = [0] * 27
        i = 25

        while i >= 0:
            deleteAll = count[i]

            if target > count[i]:
                changeOps = target - count[i]
            else:
                changeOps = count[i] - target

            val1 = deleteAll
            val2 = changeOps + dpArr[i + 1]
            currentMin = val1
            if val2 < currentMin:
                currentMin = val2

            if (i + 1) < 26 and count[i + 1] < target:
                deficitNext = target - count[i + 1]
                if count[i] <= target:
                    needChange = count[i]
                else:
                    needChange = count[i] - target

                if deficitNext > needChange:
                    changeToTargetVal = needChange + (deficitNext - needChange)
                else:
                    changeToTargetVal = deficitNext + (needChange - deficitNext)

                val3 = changeToTargetVal + dpArr[i + 2]
                if val3 < currentMin:
                    currentMin = val3

            dpArr[i] = currentMin
            i -= 1

        return dpArr[0]