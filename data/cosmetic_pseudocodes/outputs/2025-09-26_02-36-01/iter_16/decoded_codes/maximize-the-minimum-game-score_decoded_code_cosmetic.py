class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            n1 = 0
            n2 = 0
            j = 0
            length = len(points)
            while j < length:
                p = points[j]
                t1 = (minVal - 1 + p) // p  # integer division as per pseudocode
                t2 = t1 - n2
                r1 = 0 if t2 < 0 else t2
                if r1 > 0:
                    n1 += 2 * r1 - 1
                    n2 = r1 - 1
                else:
                    if j + 1 < length:
                        n1 += 1
                        n2 = 0
                if n1 > m:
                    return False
                j += 1
            return True

        a = 0
        b = (((m + 1) // 2) * points[0]) + 1

        while a < b:
            c = (a + b + 1) // 2
            if isPossible(c, m):
                a = c
            else:
                b = c - 1
        return a