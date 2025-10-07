from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:

        def arrangeAscendingByFirstElement(lst: List[Tuple[int, int]]):
            # Bubble sort for ascending order by first element
            while True:
                flagSorted = True
                index = 1
                while index < len(lst):
                    if lst[index - 1][0] > lst[index][0]:
                        lst[index - 1], lst[index] = lst[index], lst[index - 1]
                        flagSorted = False
                    index += 1
                if flagSorted:
                    break

        arrangeAscendingByFirstElement(points)

        count_rectangles = 0
        boundaryX = -1  # initializes as (0*1)-1

        def processPoints(idx: int, total: int) -> int:
            nonlocal boundaryX
            if idx >= len(points):
                return total
            pointX = points[idx][0]

            if not (pointX <= boundaryX):
                boundaryX = pointX + w
                return processPoints(idx + 1, total + 1)
            else:
                return processPoints(idx + 1, total)

        result = processPoints(0, count_rectangles)

        return result