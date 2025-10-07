from typing import List

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Solution:

    def numberOfPairs(self, points: List[Point]) -> int:

        def customSort(array: List[Point]) -> None:
            def compare(a: Point, b: Point) -> int:
                if a.x < b.x:
                    return -1
                elif a.x > b.x:
                    return 1
                else:
                    if a.y > b.y:
                        return -1
                    elif a.y < b.y:
                        return 1
                    else:
                        return 0

            def swap(p: int, q: int) -> None:
                array[p], array[q] = array[q], array[p]

            def partition(low: int, high: int) -> int:
                pivot = array[high]
                i = low - 1
                for j in range(low, high):
                    if compare(array[j], pivot) <= 0:
                        i += 1
                        swap(i, j)
                swap(i + 1, high)
                return i + 1

            stack = [(0, len(array) - 1)]

            while stack:
                start, end_ = stack.pop()
                if start < end_:
                    pivotIndex = partition(start, end_)
                    stack.append((start, pivotIndex - 1))
                    stack.append((pivotIndex + 1, end_))

        customSort(points)

        accumulator = 0
        lenPoints = len(points)

        def retrieveX(point: Point) -> int:
            return point.x

        def retrieveY(point: Point) -> int:
            return point.y

        cursor1 = 0
        while cursor1 < lenPoints:
            cursor2 = cursor1 + 1
            while cursor2 < lenPoints:
                firstX = retrieveX(points[cursor1])
                firstY = retrieveY(points[cursor1])
                secondX = retrieveX(points[cursor2])
                secondY = retrieveY(points[cursor2])

                conditionCheck = (firstX <= secondX) and (firstY >= secondY)

                if not conditionCheck:
                    cursor2 += 1
                    continue

                stateFlag = True
                cursor3 = cursor1 + 1
                while cursor3 < cursor2 and stateFlag:
                    midX = retrieveX(points[cursor3])
                    midY = retrieveY(points[cursor3])

                    if (firstX <= midX <= secondX) and (secondY <= midY <= firstY):
                        stateFlag = False
                    cursor3 += 1

                if stateFlag:
                    accumulator += 1

                cursor2 += 1
            cursor1 += 1

        return accumulator