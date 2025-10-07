class Solution:
    def makeStringGood(self, s: str) -> int:
        frequency = [0] * 26
        for ch in s:
            frequency[ord(ch) - ord('a')] += 1

        maxFreq = 0
        for freq in frequency:
            if freq > maxFreq:
                maxFreq = freq

        candidates = []
        for t in range(1, maxFreq + 1):
            candidates.append(self._getMinOperations(frequency, t))

        minOperationCount = candidates[0]
        for op in candidates[1:]:
            if op < minOperationCount:
                minOperationCount = op

        return minOperationCount

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dp = [0] * 27
        idx = 25
        while idx >= 0:
            deleteAll = count[idx]

            diff = abs(target - count[idx])

            dpOption1 = min(deleteAll, diff + dp[idx + 1])

            if idx + 1 < 26 and count[idx + 1] < target:
                nextDeficit = target - count[idx + 1]

                if count[idx] <= target:
                    needChange = count[idx]
                else:
                    needChange = count[idx] - target

                if nextDeficit > needChange:
                    changeCost = needChange + (nextDeficit - needChange)
                else:
                    changeCost = nextDeficit + (needChange - nextDeficit)

                dpOption2 = min(dpOption1, changeCost + dp[idx + 2])
                dp[idx] = dpOption2
            else:
                dp[idx] = dpOption1

            idx -= 1

        return dp[0]