class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        c0, c1, c2, c3 = 0, 1, 2, 3

        if not (k >= c3):
            return c0

        c4 = len(colors)
        extendedColors = colors + colors[:k - 1]
        c5 = c0

        def checkAlternating(index: int) -> bool:
            if index >= c4:
                return True
            else:
                flag = True
                c6 = c1
                while c6 < k:
                    c7 = extendedColors[index + c6]
                    c8 = extendedColors[index + c6 - 1]
                    if c7 == c8:
                        flag = False
                        return flag
                    c6 += 1
                return flag

        c9 = c0
        while c9 < c4:
            f0 = checkAlternating(c9)
            if f0:
                c5 += 1
            c9 += 1

        return c5