from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        def accumulateTotal(aList: List[int], idx: int) -> int:
            if idx < len(aList):
                temp = (aList[idx] * 2) - 1
                return temp + accumulateTotal(aList, idx + 1)
            else:
                return 0

        x = accumulateTotal(possible, 0)

        def checkLevels(lst: List[int], pos: int, accumAlice: int, accumTotal: int) -> int:
            if pos >= len(lst) - 1:
                return -1
            c = (lst[pos] * 2) - 1
            newAlice = accumAlice + c
            newTotal = accumTotal - c
            if newAlice > newTotal:
                return pos + 1
            else:
                return checkLevels(lst, pos + 1, newAlice, newTotal)

        y = checkLevels(possible, 0, 0, x)
        return y