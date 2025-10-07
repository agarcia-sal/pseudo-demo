class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def in_circle(x, y, cx, cy, r):
            deltaX = x - cx
            deltaY = y - cy
            distSquared = deltaX * deltaX + deltaY * deltaY
            radiusSquared = r * r
            return distSquared <= radiusSquared

        def cross_left_top(cx, cy, r):
            condOne = abs(cx) <= r and 0 <= cy <= yCorner
            diffCyTop = abs(cy - yCorner)
            condTwo = diffCyTop <= r and 0 <= cx <= xCorner
            return condOne or condTwo

        def cross_right_bottom(cx, cy, r):
            diffCxRight = abs(cx - xCorner)
            condA = diffCxRight <= r and 0 <= cy <= yCorner
            condB = abs(cy) <= r and 0 <= cx <= xCorner
            return condA or condB

        totalCircles = len(circles)
        vis = [False] * totalCircles

        def dfs(i):
            cx_i, cy_i, radius_i = circles[i]
            if cross_right_bottom(cx_i, cy_i, radius_i):
                return True
            vis[i] = True

            for index in range(totalCircles):
                if vis[index]:
                    continue
                cx_j, cy_j, radius_j = circles[index]
                dx = cx_i - cx_j
                dy = cy_i - cy_j
                distSqr = dx * dx + dy * dy
                radiusSum = radius_i + radius_j
                radiusSumSqr = radiusSum * radiusSum

                if distSqr > radiusSumSqr:
                    continue

                condX = (cx_i * radius_j) + (cx_j * radius_i) < radiusSum * xCorner
                condY = (cy_i * radius_j) + (cy_j * radius_i) < radiusSum * yCorner

                if condX and condY and dfs(index):
                    return True
            return False

        for idx, (cX, cY, rC) in enumerate(circles):
            if in_circle(0, 0, cX, cY, rC) or in_circle(xCorner, yCorner, cX, cY, rC):
                return False
            if not vis[idx] and cross_left_top(cX, cY, rC) and dfs(idx):
                return False

        return True