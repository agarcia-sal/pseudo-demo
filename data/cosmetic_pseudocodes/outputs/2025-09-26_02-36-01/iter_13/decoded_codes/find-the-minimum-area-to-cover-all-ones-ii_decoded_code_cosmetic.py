from math import inf
from typing import List, Tuple

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:

        def collectOnes(rowIndex: int, colIndex: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if rowIndex >= len(grid):
                return acc

            def innerCollect(ci: int, acc2: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if ci >= len(grid[rowIndex]):
                    return acc2
                # The pseudocode checks (grid[rowIndex][ci] == 1) and (grid[rowIndex] == 1)
                # The second condition is likely a mistake since grid[rowIndex] is a list
                # We interpret that as the first condition alone.
                if grid[rowIndex][ci] == 1:
                    return innerCollect(ci + 1, acc2 + [(rowIndex, ci)])
                else:
                    return innerCollect(ci + 1, acc2)

            return collectOnes(rowIndex + 1, 0, innerCollect(0, acc))

        H9W3 = collectOnes(0, 0, [])

        def computeRectangleArea(points: List[Tuple[int,int]]) -> int:
            if len(points) == 0:
                return 0

            def foldMinI(arr: List[Tuple[int,int]], idx: int, acc: int) -> int:
                if idx >= len(arr):
                    return acc
                return foldMinI(arr, idx + 1, min(acc, arr[idx][0]))

            def foldMaxI(arr: List[Tuple[int,int]], idx: int, acc: int) -> int:
                if idx >= len(arr):
                    return acc
                return foldMaxI(arr, idx + 1, max(acc, arr[idx][0]))

            def foldMinJ(arr: List[Tuple[int,int]], idx: int, acc: int) -> int:
                if idx >= len(arr):
                    return acc
                return foldMinJ(arr, idx + 1, min(acc, arr[idx][1]))

            def foldMaxJ(arr: List[Tuple[int,int]], idx: int, acc: int) -> int:
                if idx >= len(arr):
                    return acc
                return foldMaxJ(arr, idx + 1, max(acc, arr[idx][1]))

            minI = foldMinI(points, 0, points[0][0])
            maxI = foldMaxI(points, 0, points[0][0])
            minJ = foldMinJ(points, 0, points[0][1])
            maxJ = foldMaxJ(points, 0, points[0][1])

            width = (maxI - minI) + 1
            height = (maxJ - minJ) + 1
            return width * height

        resultSoFar = inf
        totalPoints = len(H9W3)

        def subloops(a: int, b: int, c: int) -> None:
            nonlocal resultSoFar

            if a > totalPoints:
                return
            if b > totalPoints:
                subloops(a + 1, a + 2, a + 3)
                return
            if c > totalPoints:
                subloops(a, b + 1, b + 2)
                return

            def combinations(collection: List[Tuple[int,int]], r: int) -> List[List[Tuple[int,int]]]:
                def combEnum(idx: int, start: int, curr: List[Tuple[int,int]], res: List[List[Tuple[int,int]]]) -> List[List[Tuple[int,int]]]:
                    if len(curr) == r:
                        return res + [curr]
                    if start >= len(collection):
                        return res
                    return combEnum(idx + 1, start + 1, curr + [collection[start]], res) + combEnum(idx + 1, start + 1, curr, res)
                return combEnum(0, 0, [], [])

            def toSet(lst: List[Tuple[int,int]]) -> set:
                def toSetRec(i: int, s: set) -> set:
                    if i >= len(lst):
                        return s
                    return toSetRec(i + 1, s | {lst[i]})
                return toSetRec(0, set())

            def setDifference(s1: List[Tuple[int,int]], s2: set) -> List[Tuple[int,int]]:
                def diffRec(iter_: int, res: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
                    if iter_ >= len(s1):
                        return res
                    if s1[iter_] not in s2:
                        return diffRec(iter_ + 1, res + [s1[iter_]])
                    else:
                        return diffRec(iter_ + 1, res)
                return diffRec(0, [])

            allCombiA = combinations(H9W3, a)
            for combA in allCombiA:
                setA = toSet(combA)
                remainderA = setDifference(H9W3, setA)
                allCombiB = combinations(remainderA, b - a)
                for combB in allCombiB:
                    setB = toSet(combB)
                    combC = setDifference(remainderA, setB)
                    areaA = computeRectangleArea(combA)
                    areaB = computeRectangleArea(combB)
                    areaC = computeRectangleArea(combC)
                    if areaA > 0 and areaB > 0 and areaC > 0:
                        currentSum = areaA + areaB + areaC
                        if currentSum < resultSoFar:
                            resultSoFar = currentSum

            subloops(a, b, c + 1)

        subloops(1, 2, 3)

        return resultSoFar