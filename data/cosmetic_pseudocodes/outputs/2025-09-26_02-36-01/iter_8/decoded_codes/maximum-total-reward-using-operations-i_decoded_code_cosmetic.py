from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        memo = {}

        def dfs(y: int) -> int:
            if y in memo:
                return memo[y]

            def bisect_right(arr: List[int], target: int) -> int:
                low, high = 0, len(arr)
                while low < high:
                    mid = (low + high) // 2
                    if arr[mid] > target:
                        high = mid
                    else:
                        low = mid + 1
                return low

            pos = bisect_right(rewardValues, y)
            maximumReward = 0
            index = pos
            while index < len(rewardValues):
                currentVal = rewardValues[index]
                sumVal = y + currentVal
                if sumVal > y:
                    candidate = currentVal + dfs(sumVal)
                    if candidate > maximumReward:
                        maximumReward = candidate
                index += 1
            memo[y] = maximumReward
            return maximumReward

        return dfs(0)