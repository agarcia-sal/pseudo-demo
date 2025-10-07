class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        maxFreq = max(freq)
        results = []
        for target in range(1, maxFreq + 1):
            results.append(self._getMinOperations(freq, target))
        return min(results)

    def _getMinOperations(self, freq: list[int], target: int) -> int:
        dp = [0] * 27
        for position in range(25, -1, -1):
            deleteAllCost = freq[position]
            if freq[position] < target:
                gapCost = target - freq[position]
            else:
                gapCost = freq[position] - target

            optionOne = deleteAllCost
            optionTwo = gapCost + dp[position + 1]

            cost = optionOne if optionOne < optionTwo else optionTwo

            if position + 1 < 26 and freq[position + 1] < target:
                nextDeficit = target - freq[position + 1]
                if freq[position] <= target:
                    needChange = freq[position]
                else:
                    needChange = freq[position] - target

                if nextDeficit > needChange:
                    altChangeCost = needChange + (nextDeficit - needChange)
                else:
                    altChangeCost = nextDeficit + (needChange - nextDeficit)

                optionThree = altChangeCost + dp[position + 2]
                if optionThree < cost:
                    cost = optionThree

            dp[position] = cost

        return dp[0]