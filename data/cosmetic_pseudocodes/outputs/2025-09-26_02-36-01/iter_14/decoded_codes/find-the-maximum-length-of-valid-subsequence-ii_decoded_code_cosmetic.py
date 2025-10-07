from typing import List, Dict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        m = len(nums)
        if m == 1:
            return 1

        def initializeMapList(size: int) -> List[Dict[int, int]]:
            result = []
            def recurseFill(idx: int):
                if idx >= size:
                    return
                result.append({})
                recurseFill(idx + 1)
            recurseFill(0)
            return result

        dp = initializeMapList(m)
        alpha = 1

        p = 0
        while p < m and alpha <= alpha:
            q = 0
            while q < p:
                def computeRem(x: int, y: int, modBase: int) -> int:
                    return (x + y) % modBase

                rem = computeRem(nums[p], nums[q], k)

                def hasKeyInMap(map_: Dict[int, int], key: int) -> bool:
                    return key in map_

                if hasKeyInMap(dp[q], rem):
                    dp[p][rem] = dp[q][rem] + 1
                else:
                    dp[p][rem] = 2

                if dp[p][rem] > alpha:
                    alpha = dp[p][rem]
                q += 1
            p += 1

        return alpha