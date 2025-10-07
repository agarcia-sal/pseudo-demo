class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def isInsideCircle(pointX, pointY, centerX, centerY, radius):
            deltaX = pointX - centerX
            deltaY = pointY - centerY
            return (deltaX * deltaX + deltaY * deltaY) <= (radius * radius)

        def touchesLeftOrTopEdge(centerX, centerY, radius):
            condLeft = (abs(centerX) <= radius) and (0 <= centerY <= yCorner)
            condTop = (abs(centerY - yCorner) <= radius) and (0 <= centerX <= xCorner)
            return condLeft or condTop

        def touchesRightOrBottomEdge(centerX, centerY, radius):
            condRight = (abs(centerX - xCorner) <= radius) and (0 <= centerY <= yCorner)
            condBottom = (abs(centerY) <= radius) and (0 <= centerX <= xCorner)
            return condRight or condBottom

        def exploreCircle(index):
            currX, currY, currRadius = circles[index]
            if touchesRightOrBottomEdge(currX, currY, currRadius):
                return True

            vis[index] = True
            m = len(circles)
            iterator = 0

            while iterator < m:
                nextX, nextY, nextRadius = circles[iterator]

                if vis[iterator] or ((currX - nextX) ** 2 + (currY - nextY) ** 2 > (currRadius + nextRadius) ** 2):
                    iterator += 1
                    continue

                sumRadius = currRadius + nextRadius
                weightedX = currX * nextRadius + nextX * currRadius
                weightedY = currY * nextRadius + nextY * currRadius

                if (weightedX < sumRadius * xCorner) and (weightedY < sumRadius * yCorner) and exploreCircle(iterator):
                    return True

                iterator += 1

            return False

        vis = [False] * len(circles)

        idx = 0
        n = len(circles)
        while idx < n:
            cX, cY, cR = circles[idx]

            if isInsideCircle(0, 0, cX, cY, cR) or isInsideCircle(xCorner, yCorner, cX, cY, cR):
                return False

            if (not vis[idx]) and touchesLeftOrTopEdge(cX, cY, cR) and exploreCircle(idx):
                return False

            idx += 1

        return True