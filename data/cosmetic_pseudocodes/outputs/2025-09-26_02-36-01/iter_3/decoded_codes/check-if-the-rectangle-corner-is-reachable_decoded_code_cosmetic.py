class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def in_circle(x, y, cx, cy, r):
            dx = x - cx
            dy = y - cy
            distSq = dx * dx + dy * dy
            radiusSq = r * r
            return distSq <= radiusSq

        def cross_left_top(cx, cy, r):
            cond1 = (abs(cx) <= r) and (0 <= cy <= yCorner)
            cond2 = (abs(cy - yCorner) <= r) and (0 <= cx <= xCorner)
            return cond1 or cond2

        def cross_right_bottom(cx, cy, r):
            condA = (abs(cx - xCorner) <= r) and (0 <= cy <= yCorner)
            condB = (abs(cy) <= r) and (0 <= cx <= xCorner)
            return condA or condB

        def dfs(i):
            cx1, cy1, rr1 = circles[i]

            if cross_right_bottom(cx1, cy1, rr1):
                return True

            vis[i] = True

            for idx in range(len(circles)):
                if vis[idx]:
                    continue
                cx2, cy2, rr2 = circles[idx]
                distX = cx1 - cx2
                distY = cy1 - cy2
                sumRadii = rr1 + rr2
                distSquares = distX * distX + distY * distY
                radiusSumSq = sumRadii * sumRadii

                if distSquares > radiusSumSq:
                    continue

                leftBoundX = (cx1 * rr2) + (cx2 * rr1)
                rightBoundX = sumRadii * xCorner
                leftBoundY = (cy1 * rr2) + (cy2 * rr1)
                rightBoundY = sumRadii * yCorner

                if leftBoundX < rightBoundX and leftBoundY < rightBoundY:
                    if dfs(idx):
                        return True
            return False

        vis = [False] * len(circles)

        for pointer in range(len(circles)):
            cx, cy, rr = circles[pointer]

            if in_circle(0, 0, cx, cy, rr) or in_circle(xCorner, yCorner, cx, cy, rr):
                return False

            if not vis[pointer] and cross_left_top(cx, cy, rr) and dfs(pointer):
                return False

        return True