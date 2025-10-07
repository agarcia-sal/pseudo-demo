class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        moveCount = 2
        if e == a:
            if a != c:
                moveCount = 1
            else:
                if (b < d < f) or (f > d > b):
                    moveCount = 2
                else:
                    moveCount = 1
            return moveCount

        if f == b:
            if b != d:
                moveCount = 1
            else:
                if (c < a < e) or (e > a > c):
                    moveCount = 2
                else:
                    moveCount = 1
            return moveCount

        sum1 = c + d
        sum2 = e + f
        if sum1 == sum2:
            sum3 = a + b
            if sum3 != sum1:
                moveCount = 1
            else:
                condition1 = (c < a < e and d < b < f)
                condition2 = (e < a < c and f < b < d)
                if condition1 or condition2:
                    moveCount = 2
                else:
                    moveCount = 1
            return moveCount

        diff1 = c - d
        diff2 = e - f
        if diff1 == diff2:
            diff3 = a - b
            if diff3 != diff1:
                moveCount = 1
            else:
                condA = (c < a < e and d > b > f)
                condB = (e < a < c and f > b > d)
                if condA or condB:
                    moveCount = 2
                else:
                    moveCount = 1
            return moveCount

        return moveCount