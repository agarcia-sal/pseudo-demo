class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        visited = [False] * len(circles)

        def in_circle(x, y, cx, cy, r):
            deltaX = x - cx
            deltaY = y - cy
            lhs = deltaX * deltaX + deltaY * deltaY
            rhs = r * r
            return lhs <= rhs

        def cross_left_top(cx, cy, r):
            absCx = cx if cx >= 0 else -cx
            condA = absCx <= r and 0 <= cy <= yCorner

            deltaCy = cy - yCorner
            absDeltaCy = deltaCy if deltaCy >= 0 else -deltaCy
            condB = absDeltaCy <= r and 0 <= cx <= xCorner

            return condA or condB

        def cross_right_bottom(cx, cy, r):
            diffCx = cx - xCorner
            absDiffCx = diffCx if diffCx >= 0 else -diffCx
            condA = absDiffCx <= r and 0 <= cy <= yCorner

            absCy = cy if cy >= 0 else -cy
            condB = absCy <= r and 0 <= cx <= xCorner

            return condA or condB

        def dfs(i):
            circleI = circles[i]
            posX, posY, radiusI = circleI

            if cross_right_bottom(posX, posY, radiusI):
                return True

            visited[i] = True

            for idx in range(len(circles)):
                if visited[idx]:
                    continue

                circleJ = circles[idx]
                posXJ, posYJ, radiusJ = circleJ

                deltaX = posX - posXJ
                deltaY = posY - posYJ

                lhsVal = deltaX * deltaX + deltaY * deltaY
                sumRadius = radiusI + radiusJ
                rhsVal = sumRadius * sumRadius

                if lhsVal > rhsVal:
                    continue

                prod1 = posX * radiusJ
                prod2 = posXJ * radiusI
                sumRadiiXCorner = sumRadius * xCorner

                prod3 = posY * radiusJ
                prod4 = posYJ * radiusI
                sumRadiiYCorner = sumRadius * yCorner

                if (prod1 + prod2) < sumRadiiXCorner and (prod3 + prod4) < sumRadiiYCorner:
                    if dfs(idx):
                        return True
            return False

        for indexI in range(len(circles)):
            cx, cy, r = circles[indexI]
            if in_circle(0, 0, cx, cy, r):
                return False
            if in_circle(xCorner, yCorner, cx, cy, r):
                return False
            if not visited[indexI]:
                if cross_left_top(cx, cy, r):
                    if dfs(indexI):
                        return False

        return True