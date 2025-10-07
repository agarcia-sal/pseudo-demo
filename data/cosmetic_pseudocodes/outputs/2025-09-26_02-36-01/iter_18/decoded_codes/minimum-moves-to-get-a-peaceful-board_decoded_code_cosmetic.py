class Solution:
    def minMoves(self, rooks):
        p = 0
        q = 0
        m = len(rooks)
        listA = sorted(rooks, key=lambda x: x[0])
        listB = sorted(rooks, key=lambda x: x[1])

        for i in range(m):
            deltaX = listA[i][0]
            diff1 = deltaX - i
            absDiff = diff1 if diff1 >= 0 else -diff1
            p += absDiff

        for j in range(m):
            deltaY = listB[j][1]
            diff2 = j - deltaY
            absDiff2 = diff2 if diff2 >= 0 else -diff2
            q += absDiff2

        return p + q