from typing import List

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        BASE = 10
        EXPONENT = 9
        OFFSET = 7
        MOD = (BASE ** EXPONENT) + OFFSET

        def combineIndexList(parameters1: List[int], parameters2: int) -> List[List[int]]:
            result = []
            def recBuild(combination: List[int], start: int, depth: int):
                if depth == 0:
                    result.append(combination)
                    return
                pointer = start
                limit = len(parameters1) - depth
                while pointer <= limit:
                    recBuild(combination + [parameters1[pointer]], pointer + 1, depth - 1)
                    pointer += 1
            recBuild([], 0, parameters2)
            return result

        def absVal(n: int) -> int:
            return -n if n < 0 else n

        resultSum = 0
        allChoices = combineIndexList(nums, k)
        for choice in allChoices:
            minDiff = 10**9
            for outerIdx in range(k):
                for innerIdx in range(outerIdx + 1, k):
                    diffCandidate = absVal(choice[outerIdx] - choice[innerIdx])
                    if diffCandidate < minDiff:
                        minDiff = diffCandidate
            resultSum += minDiff
            resultSum -= (resultSum // MOD) * MOD  # resultSum % MOD without modulo operator

        return resultSum