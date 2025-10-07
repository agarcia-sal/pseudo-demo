class Solution:
    def minRectanglesToCoverPoints(self, points, w):
        sortedPoints = sorted(points, key=lambda p: p[0])
        countRectangles = 0
        limitX = -1
        idx = 0
        n = len(sortedPoints)
        while idx < n:
            xCoord, yCoord = sortedPoints[idx]
            if xCoord > limitX:
                limitX = xCoord + w
                countRectangles += 1
            idx += 1
        return countRectangles