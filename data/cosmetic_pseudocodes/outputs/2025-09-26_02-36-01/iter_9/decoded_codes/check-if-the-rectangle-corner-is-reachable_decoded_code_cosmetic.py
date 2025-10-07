class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def isInsideCircle(pX, pY, cX, cY, radius):
            deltaX = pX - cX
            deltaY = pY - cY
            distSquared = deltaX * deltaX + deltaY * deltaY
            radiusSq = radius * radius
            return distSquared <= radiusSq

        def intersectsLeftTop(cX, cY, r):
            cond1 = (abs(cX) <= r) and (0 <= cY <= yCorner)
            cond2 = (abs(cY - yCorner) <= r) and (0 <= cX <= xCorner)
            return cond1 or cond2

        def intersectsRightBottom(cX, cY, r):
            condA = (abs(cX - xCorner) <= r) and (0 <= cY <= yCorner)
            condB = (abs(cY) <= r) and (0 <= cX <= xCorner)
            return condA or condB

        def explore(idx):
            posX, posY, rad = circles[idx]

            if intersectsRightBottom(posX, posY, rad):
                return True

            vis[idx] = True

            for controlIdx, circleData in enumerate(circles):
                if vis[controlIdx]:
                    continue

                cx, cy, cr = circleData
                distanceX = posX - cx
                distanceY = posY - cy
                sumRadius = rad + cr

                if distanceX * distanceX + distanceY * distanceY > sumRadius * sumRadius:
                    continue

                checkX = (posX * cr) + (cx * rad)
                limitX = sumRadius * xCorner
                checkY = (posY * cr) + (cy * rad)
                limitY = sumRadius * yCorner

                if checkX < limitX and checkY < limitY and explore(controlIdx):
                    return True

            return False

        vis = [False] * len(circles)

        for iterator in range(len(circles)):
            circleX, circleY, circleR = circles[iterator]

            if isInsideCircle(0, 0, circleX, circleY, circleR) or isInsideCircle(xCorner, yCorner, circleX, circleY, circleR):
                return False

            if not vis[iterator] and intersectsLeftTop(circleX, circleY, circleR) and explore(iterator):
                return False

        return True