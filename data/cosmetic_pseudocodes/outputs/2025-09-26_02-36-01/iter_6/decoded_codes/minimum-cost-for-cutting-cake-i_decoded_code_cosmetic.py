from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def reverseSortDesc(lst: List[int]) -> List[int]:
            def helper(k: int, acc: List[int]) -> List[int]:
                if k < len(lst):
                    # Append elements from the end to accumulate in reversed order
                    return helper(k + 1, [lst[len(lst) - k - 1]] + acc)
                else:
                    return acc
            return helper(0, [])

        hRev = reverseSortDesc(horizontalCut)
        vRev = reverseSortDesc(verticalCut)

        totalSum = 0
        indexH = 0
        indexV = 0
        countH = 1
        countV = 1

        def loopIter(ic: int, ic2: int, cH: int, cV: int, accum: int) -> int:
            if not (ic >= m - 1 or ic2 >= n - 1):
                if (ic2 == n - 1) or (ic < m - 1 and hRev[ic] > vRev[ic2]):
                    partCalc = hRev[ic] * cV
                    accum2 = accum + partCalc
                    return loopIter(ic + 1, ic2, cH + 1, cV, accum2)
                else:
                    partCalc2 = vRev[ic2] * cH
                    accum3 = accum + partCalc2
                    return loopIter(ic, ic2 + 1, cH, cV + 1, accum3)
            else:
                return accum

        return loopIter(indexH, indexV, countH, countV, totalSum)