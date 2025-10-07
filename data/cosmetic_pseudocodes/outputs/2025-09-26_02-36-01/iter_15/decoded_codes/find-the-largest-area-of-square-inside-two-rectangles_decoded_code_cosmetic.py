class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            a0 = bl1[0]
            b0 = bl2[0]
            c0 = tr1[0]
            d0 = tr2[0]

            l0 = a0 if a0 > b0 else b0
            r0 = c0 if c0 < d0 else d0

            a1 = bl1[1]
            b1 = bl2[1]
            c1 = tr1[1]
            d1 = tr2[1]

            btm = a1 if a1 > b1 else b1
            tp = c1 if c1 < d1 else d1

            if l0 >= r0 or btm >= tp:
                return 0
            else:
                widthDiff = r0 - l0
                heightDiff = tp - btm
                sideLen = widthDiff if widthDiff < heightDiff else heightDiff
                res = 0
                idx = 0
                while idx < sideLen:
                    res += sideLen
                    idx += 1
                return res

        result = 0
        n = len(bottomLeft)
        for k0 in range(n):
            length = k0 + 1
            while length < n:
                currArea = intersecting_square_area(
                    bottomLeft[k0], topRight[k0],
                    bottomLeft[length], topRight[length]
                )
                if currArea > result:
                    result = currArea
                length += 1
        return result