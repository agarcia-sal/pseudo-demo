from typing import List

def bisect_right_sorted_position(arr: List[int], val: int) -> int:
    leftBound = 0
    rightBound = len(arr)
    while leftBound < rightBound:
        middleIndex = (leftBound + rightBound) // 2
        if val <= arr[middleIndex]:
            leftBound = middleIndex + 1
        else:
            rightBound = middleIndex
    return leftBound

def sort_ascending(arr: List[int]) -> None:
    x_idx = 1
    while x_idx < len(arr):
        y_val = arr[x_idx]
        y_pos = x_idx
        while y_pos > 0 and arr[y_pos - 1] > y_val:
            arr[y_pos] = arr[y_pos - 1]
            y_pos -= 1
        arr[y_pos] = y_val
        x_idx += 1

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        sort_ascending(rewardValues)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(p: int) -> int:
            w = bisect_right_sorted_position(rewardValues, p)
            h = 0
            z = w
            while z < len(rewardValues):
                q = rewardValues[z]
                if (p + q) > p:  # equivalent to not (p+q <= p)
                    m = dfs(p + q)
                    r = q + m
                    if r > h:
                        h = r
                z += 1
            return h

        return dfs(0)