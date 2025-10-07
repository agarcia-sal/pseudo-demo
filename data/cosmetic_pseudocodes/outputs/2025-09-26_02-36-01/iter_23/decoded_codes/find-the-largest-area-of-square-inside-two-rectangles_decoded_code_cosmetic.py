from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(xB1: Tuple[int, int], xT1: Tuple[int, int],
                                    xB2: Tuple[int, int], xT2: Tuple[int, int]) -> int:
            def maxVal(a: int, b: int) -> int:
                return a if a > b else b

            def minVal(a: int, b: int) -> int:
                return a if a < b else b

            u1 = maxVal(xB1[0], xB2[0])
            v1 = minVal(xT1[0], xT2[0])
            u2 = maxVal(xB1[1], xB2[1])
            v2 = minVal(xT1[1], xT2[1])

            def isNoOverlap(a: int, b: int, c: int, d: int) -> bool:
                return (a >= b) or (c >= d)

            if isNoOverlap(u1, v1, u2, v2):
                return 0  # no overlap area

            def calcSide(x: int, y: int) -> int:
                return x if x < y else y

            sideCandidateA = v1 - u1
            sideCandidateB = v2 - u2
            sideLength = calcSide(sideCandidateA, sideCandidateB)
            resultingArea = sideLength * sideLength
            return resultingArea

        def iterate_j(index_i: int, limit_n: int, acc_area: int) -> int:
            if index_i >= limit_n:
                return acc_area

            def iterate_inner(index_j: int, acc_inner: int) -> int:
                if index_j >= limit_n:
                    return acc_inner
                areaNow = intersecting_square_area(
                    bottomLeft[index_i], topRight[index_i],
                    bottomLeft[index_j], topRight[index_j]
                )
                acc_inner_updated = acc_inner
                if areaNow > acc_inner:
                    acc_inner_updated = areaNow
                return iterate_inner(index_j + 1, acc_inner_updated)

            maxFound = iterate_inner(index_i + 1, acc_area)
            return iterate_j(index_i + 1, limit_n, maxFound)

        length_n = len(bottomLeft)
        resultMax = iterate_j(0, length_n, 0)
        return resultMax