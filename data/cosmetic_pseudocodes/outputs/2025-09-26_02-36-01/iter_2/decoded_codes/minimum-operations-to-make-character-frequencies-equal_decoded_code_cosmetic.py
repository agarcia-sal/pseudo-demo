class Solution:
    def makeStringGood(self, s: str) -> int:
        frequency = [0] * 26
        idx = 0
        while idx < len(s):
            ch = s[idx]
            pos = ord(ch) - ord('a')
            frequency[pos] += 1
            idx += 1

        maxCount = 0
        for value in frequency:
            if value > maxCount:
                maxCount = value

        minimumOperations = None
        t = 1
        while t <= maxCount:
            candidateOps = self._getMinOperations(frequency, t)
            if minimumOperations is None or candidateOps < minimumOperations:
                minimumOperations = candidateOps
            t += 1

        return minimumOperations

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dp = [0] * 27
        i = 25
        while i >= 0:
            deleteAll = count[i]
            if target > count[i]:
                diffDeleteInsert = target - count[i]
            else:
                diffDeleteInsert = count[i] - target

            withNextStep = diffDeleteInsert + dp[i + 1]
            currentMin = deleteAll
            if withNextStep < currentMin:
                currentMin = withNextStep

            if (i + 1) < 26:
                if count[i + 1] < target:
                    deficitNext = target - count[i + 1]

                    if count[i] <= target:
                        needChange = count[i]
                    else:
                        needChange = count[i] - target

                    if deficitNext > needChange:
                        changeCost = needChange + (deficitNext - needChange)
                    else:
                        changeCost = deficitNext + (needChange - deficitNext)

                    candidateVal = changeCost + dp[i + 2]
                    if candidateVal < currentMin:
                        currentMin = candidateVal

            dp[i] = currentMin
            i -= 1

        return dp[0]