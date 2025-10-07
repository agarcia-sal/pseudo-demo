class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            alpha = 0
            beta = 0

            def ceilDiv(a, b):
                return (a + b - 1) // b

            idx = 0
            n = len(points)
            while idx < n:
                curr = points[idx]
                calc = ceilDiv(minVal + curr - 1, curr)
                diff = calc - beta if (calc - beta) >= 0 else 0

                if diff > 0:
                    alpha += (2 * diff - 1)
                    beta = diff - 1
                else:
                    if idx + 1 < n:
                        alpha += 1
                        beta = 0

                if alpha > m:
                    return False
                idx += 1
            return True

        lowerBound = 0
        upperBound = (((m + 1) // 2) * points[0]) + 1

        def binarySearch(l, r):
            if l < r:
                median = (l + r + 1) // 2
                if isPossible(median, m):
                    return binarySearch(median, r)
                else:
                    return binarySearch(l, median - 1)
            else:
                return l

        return binarySearch(lowerBound, upperBound)