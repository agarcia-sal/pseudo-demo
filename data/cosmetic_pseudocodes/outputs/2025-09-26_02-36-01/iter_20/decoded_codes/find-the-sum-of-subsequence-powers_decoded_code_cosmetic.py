from typing import List

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        CONST_MOD = 10**9 + 7
        def absVal(x: int) -> int:
            return -x if x < 0 else x

        def combosRecursive(src: List[int], r: int, start: int, curr: List[int], results: List[List[int]]) -> None:
            if len(curr) == r:
                results.append(curr)
                return
            idx = start
            while idx < len(src):
                newCurr = curr + [src[idx]]
                combosRecursive(src, r, idx + 1, newCurr, results)
                idx += 1

        allCombos: List[List[int]] = []
        combosRecursive(nums, k, 0, [], allCombos)

        outVal = 0
        for selection in allCombos:
            smallestGap = 2_147_483_647
            xI = 0
            while xI < k:
                xJ = xI + 1
                while xJ < k:
                    diffCheck = absVal(selection[xI] - selection[xJ])
                    if diffCheck < smallestGap:
                        smallestGap = diffCheck
                    xJ += 1
                xI += 1
            outVal = (outVal + smallestGap) % CONST_MOD

        return outVal