from math import inf
from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        lengthNums = len(nums)
        ans = []

        def absDiff(a: int, b: int) -> int:
            return a - b if a >= b else b - a

        def isMaskFull(m: int) -> bool:
            return m == (1 << lengthNums) - 1

        def dfs(mask: int, pre: int) -> int:
            if isMaskFull(mask):
                return absDiff(pre, nums[0])  # close the loop
            else:
                def dfsLoop(curIdx: int, resAcc: int) -> int:
                    if curIdx == lengthNums:
                        return resAcc
                    def isNotVisited(m: int, idx: int) -> bool:
                        return ((m >> idx) & 1) == 0
                    if isNotVisited(mask, curIdx):
                        tempCandidate = absDiff(pre, nums[curIdx]) + dfs(mask | (1 << curIdx), curIdx)
                        if tempCandidate < resAcc:
                            return dfsLoop(curIdx + 1, tempCandidate)
                        else:
                            return dfsLoop(curIdx + 1, resAcc)
                    else:
                        return dfsLoop(curIdx + 1, resAcc)
                return dfsLoop(0, inf)

        def generate(mask: int, pre: int) -> None:
            def appendAns(val: int) -> None:
                nonlocal ans
                ans.append(val)

            def isMaskComplete(m: int) -> bool:
                return m == (1 << lengthNums) - 1

            def recurLoop(i: int) -> None:
                if i == lengthNums:
                    return
                def isFree(m: int, idx: int) -> bool:
                    return ((m >> idx) & 1) == 0
                if isFree(mask, i):
                    potential = absDiff(pre, nums[i]) + dfs(mask | (1 << i), i)
                    if potential == dfs(mask, pre):
                        generate(mask | (1 << i), i)
                        return
                    else:
                        recurLoop(i + 1)
                else:
                    recurLoop(i + 1)

            appendAns(pre)
            if isMaskComplete(mask):
                return
            recurLoop(0)

        generate(1 << 0, 0)
        return ans