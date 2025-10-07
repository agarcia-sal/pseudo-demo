class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def insideCircle(a, b, c, d, e):
            return (a - c) ** 2 + (b - d) ** 2 <= e ** 2

        def overlapsLeftTop(p, q, s):
            condOne = (abs(p) <= s) and (0 <= q <= yCorner)
            condTwo = (abs(q - yCorner) <= s) and (0 <= p <= xCorner)
            return condOne or condTwo

        def overlapsRightBottom(u, v, w):
            condA = (abs(u - xCorner) <= w) and (0 <= v <= yCorner)
            condB = (abs(v) <= w) and (0 <= u <= xCorner)
            return condA or condB

        def explore(index):
            cx, cy, radius = circles[index]
            if overlapsRightBottom(cx, cy, radius):
                return True

            vis[index] = True

            def checkNext(j):
                nx, ny, nr = circles[j]
                distSq = (cx - nx) ** 2 + (cy - ny) ** 2
                radiusSum = radius + nr
                intersecting = distSq <= radiusSum ** 2
                if vis[j] or not intersecting:
                    return False

                leftSideX = cx * nr + nx * radius
                rightSideX = radiusSum * xCorner
                leftSideY = cy * nr + ny * radius
                rightSideY = radiusSum * yCorner

                if leftSideX < rightSideX and leftSideY < rightSideY and explore(j):
                    return True
                return False

            for k in range(len(circles)):
                if checkNext(k):
                    return True
            return False

        vis = [False] * len(circles)
        idx = 0
        while idx < len(circles):
            cx, cy, radius = circles[idx]
            if insideCircle(0, 0, cx, cy, radius) or insideCircle(xCorner, yCorner, cx, cy, radius):
                return False
            if not vis[idx] and overlapsLeftTop(cx, cy, radius) and explore(idx):
                return False
            idx += 1
        return True