class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(blA, trA, blB, trB):
            def maxVal(a, b):
                return a if a > b else b

            def minVal(a, b):
                return a if a < b else b

            c1 = maxVal(blA[0], blB[0])
            c2 = minVal(trA[0], trB[0])
            c3 = maxVal(blA[1], blB[1])
            c4 = minVal(trA[1], trB[1])

            if c1 >= c2 or c3 >= c4:
                return 0

            tempSide1 = c2 - c1
            tempSide2 = c4 - c3

            def lesser(x, y):
                return x if x < y else y

            side_len = lesser(tempSide1, tempSide2)
            sideSquared = side_len * side_len
            return sideSquared

        result_area = 0
        limit = 0
        while limit < len(bottomLeft):
            inner_idx = limit + 1
            while inner_idx < len(bottomLeft):
                area_candidate = intersecting_square_area(
                    bottomLeft[limit], topRight[limit], bottomLeft[inner_idx], topRight[inner_idx]
                )
                if area_candidate > result_area:
                    result_area = area_candidate
                inner_idx += 1
            limit += 1

        return result_area