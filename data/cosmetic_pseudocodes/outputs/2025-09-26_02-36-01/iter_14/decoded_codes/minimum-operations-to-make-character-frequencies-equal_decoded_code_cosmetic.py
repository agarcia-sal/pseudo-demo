from typing import List

class Solution:
    def makeStringGood(self, s: str) -> int:
        freqArray = [0] * 26
        for ch in s:
            freqArray[ord(ch) - ord('a')] += 1

        maxCount = max(freqArray)

        def helper(targetFreq: int) -> int:
            dpList = [0] * 27
            i = 25
            while i >= 0:
                delAll = freqArray[i]
                diffVal = abs(targetFreq - freqArray[i])

                val1 = min(delAll, diffVal + dpList[i + 1])

                if (i + 1) < 26 and freqArray[i + 1] < targetFreq:
                    diffNext = targetFreq - freqArray[i + 1]

                    if freqArray[i] <= targetFreq:
                        needChange = freqArray[i]
                    else:
                        needChange = freqArray[i] - targetFreq

                    if diffNext > needChange:
                        changeVal = needChange + (diffNext - needChange)
                    else:
                        changeVal = diffNext + (needChange - diffNext)

                    val1 = min(val1, changeVal + dpList[i + 2])

                dpList[i] = val1
                i -= 1
            return dpList[0]

        minOps = helper(1)
        targetNum = 2
        while targetNum <= maxCount:
            currOps = helper(targetNum)
            if currOps < minOps:
                minOps = currOps
            targetNum += 1

        return minOps

    def _getMinOperations(self, count: List[int], target: int) -> int:
        dpList = [0] * 27
        iterIdx = 25
        while iterIdx >= 0:
            delFull = count[iterIdx]
            diffCalc = abs(target - count[iterIdx])

            candidate1 = min(delFull, diffCalc + dpList[iterIdx + 1])

            if (iterIdx + 1) < 26 and count[iterIdx + 1] < target:
                deficitNext = target - count[iterIdx + 1]

                if count[iterIdx] <= target:
                    needChangeVal = count[iterIdx]
                else:
                    needChangeVal = count[iterIdx] - target

                if deficitNext > needChangeVal:
                    candidate2 = needChangeVal + (deficitNext - needChangeVal)
                else:
                    candidate2 = deficitNext + (needChangeVal - deficitNext)

                candidate1 = min(candidate1, candidate2 + dpList[iterIdx + 2])

            dpList[iterIdx] = candidate1
            iterIdx -= 1

        return dpList[0]