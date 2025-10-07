class Solution:
    def makeStringGood(self, s: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        max_count = max(count) if count else 0
        minimum_operations = min(self._getMinOperations(count, target) for target in range(1, max_count + 1))
        return minimum_operations

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dp = [0] * 27
        for i in range(25, -1, -1):
            deleteAllToZero = count[i]
            if target > count[i]:
                deleteOrInsertToTarget = target - count[i]
            else:
                deleteOrInsertToTarget = count[i] - target

            dp_at_i = min(deleteAllToZero, deleteOrInsertToTarget + dp[i + 1])

            if i + 1 < 26 and count[i + 1] < target:
                nextDeficit = target - count[i + 1]
                needToChange = count[i] if count[i] <= target else count[i] - target

                if nextDeficit > needToChange:
                    changeToTarget = needToChange + (nextDeficit - needToChange)
                else:
                    changeToTarget = nextDeficit + (needToChange - nextDeficit)

                dp_at_i = min(dp_at_i, changeToTarget + dp[i + 2])

            dp[i] = dp_at_i
        return dp[0]