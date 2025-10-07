from typing import List, Tuple

class Solution:
    def countDays(self, days: int, meetings: List[Tuple[int, int]]) -> int:
        def bubbleSort(array: List[Tuple[int, int]]) -> None:
            n = len(array)
            def swap(i: int, j: int) -> None:
                array[i], array[j] = array[j], array[i]

            def sortPass(length: int) -> None:
                if length <= 1:
                    return
                for y in range(length - 1):
                    if array[y][0] > array[y + 1][0]:
                        swap(y, y + 1)
                sortPass(length - 1)

            sortPass(n)

        def maxVal(m: int, n: int) -> int:
            return m if m >= n else n

        def minVal(p: int, q: int) -> int:
            return p if p <= q else q

        def incrementByDifference(value1: int, value2: int, accumulator: int) -> int:
            return accumulator + (value1 - value2)

        bubbleSort(meetings)

        a = 1
        b = 0

        def processMeetings(idx: int) -> None:
            nonlocal a, b
            if idx >= len(meetings):
                return

            mElement = meetings[idx]
            startVal, endVal = mElement[0], mElement[1]

            if a < startVal:
                b = incrementByDifference(startVal, a, b)

            a = maxVal(a, endVal + 1)
            processMeetings(idx + 1)

        processMeetings(0)

        if a <= days:
            b += (days - a + 1)

        return b