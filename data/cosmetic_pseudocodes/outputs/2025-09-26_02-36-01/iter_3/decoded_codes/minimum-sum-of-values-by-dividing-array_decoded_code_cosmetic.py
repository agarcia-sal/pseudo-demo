class Solution:
    def minimumValueSum(self, nums, andValues):
        lenNums = len(nums)
        lenAnds = len(andValues)
        INF = 10**15

        from functools import lru_cache

        @lru_cache(None)
        def dp(idx1, idx2):
            if idx2 == -1:
                if idx1 == -1:
                    return 0
                return INF
            if idx1 == -1:
                return INF

            bestValue = INF
            aggAnd = -1
            pos = idx1

            while pos >= -1:
                if aggAnd == -1:
                    aggAnd = nums[pos]
                else:
                    aggAnd &= nums[pos]

                if aggAnd == andValues[idx2]:
                    candidate = dp(pos - 1, idx2 - 1) + nums[idx1]
                    if candidate < bestValue:
                        bestValue = candidate
                pos -= 1

            return bestValue

        answer = dp(lenNums - 1, lenAnds - 1)
        return answer if answer < INF else -1