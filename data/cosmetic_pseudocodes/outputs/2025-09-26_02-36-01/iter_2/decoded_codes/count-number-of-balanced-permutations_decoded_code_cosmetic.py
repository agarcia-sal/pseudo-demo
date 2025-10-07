from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        val = num
        digitList = [int(ch) for ch in num]
        totalSum = sum(digitList)
        if totalSum % 2 != 0:
            return 0

        lengthNums = len(digitList)
        mod = 10 ** 9 + 7
        cnt = Counter(digitList)

        # Memoization decorator to optimize dfs
        from functools import lru_cache

        @lru_cache(None)
        def dfs(index: int, target: int, leftCount: int, rightCount: int) -> int:
            if index > 9:
                # When all digits used, all parameters should be zero for balanced
                return int((target | leftCount | rightCount) == 0)
            if leftCount == 0 and target != 0:
                return 0
            result = 0
            maxUse = min(cnt.get(index, 0), leftCount)
            step = 0
            while step <= maxUse:
                notUsed = cnt.get(index, 0) - step
                if 0 <= notUsed <= rightCount and step * index <= target:
                    part1 = comb(leftCount, step)
                    part2 = comb(rightCount, notUsed)
                    part3 = dfs(index + 1, target - step * index, leftCount - step, rightCount - notUsed)
                    temp = part1 * part2 * part3
                    result += temp
                step += 1
            return result % mod

        # leftCount: half length, rightCount: other half (for odd length, the right half is larger)
        return dfs(0, totalSum // 2, lengthNums // 2, (lengthNums + 1) // 2)