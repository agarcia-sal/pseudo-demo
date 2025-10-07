from typing import List

class TupleObj:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, tuples: List[TupleObj]) -> int:
        def orderList(arr: List[TupleObj]) -> None:
            n = len(arr)
            for idx1 in range(n - 1):
                for idx2 in range(idx1 + 1, n):
                    condPrimary = arr[idx1].x > arr[idx2].x
                    condSecondary = arr[idx1].x == arr[idx2].x and arr[idx1].y < arr[idx2].y
                    if condPrimary or condSecondary:
                        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        pCount = 0
        limit = len(tuples)
        orderList(tuples)

        def checkRange(startPos: int, endPos: int, baseX: int, baseY: int, boundX: int, boundY: int) -> bool:
            def verify(index: int) -> bool:
                curX = tuples[index].x
                curY = tuples[index].y
                # Return True if current point is NOT inside the defined bounding box
                return not (baseX <= curX <= boundX and boundY <= curY <= baseY)

            def recurse(curr: int) -> bool:
                if curr >= endPos:
                    return True
                if verify(curr):
                    return recurse(curr + 1)
                return False

            return recurse(startPos + 1)

        def traverse(first: int, last: int) -> None:
            nonlocal pCount
            if first < last:
                xFirst = tuples[first].x
                yFirst = tuples[first].y
                xLast = tuples[last].x
                yLast = tuples[last].y
                if xFirst <= xLast and yFirst >= yLast:
                    if checkRange(first, last, xFirst, yFirst, xLast, yLast):
                        pCount += 1
                traverse(first, last - 1)

        for startIndex in range(limit - 1):
            traverse(startIndex, limit - 1)

        return pCount