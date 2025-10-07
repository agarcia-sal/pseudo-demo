class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()  # sort rewardValues in ascending order

        def dfs(a):
            idx = 0
            n = len(rewardValues)
            while idx < n and rewardValues[idx] <= a:
                idx += 1
            result = 0
            p = idx
            while p < n:
                current = rewardValues[p]
                sumVal = a + current
                if sumVal > a:
                    temp = dfs(sumVal)
                    candidate = current + temp
                    if candidate > result:
                        result = candidate
                p += 1
            return result

        return dfs(0)