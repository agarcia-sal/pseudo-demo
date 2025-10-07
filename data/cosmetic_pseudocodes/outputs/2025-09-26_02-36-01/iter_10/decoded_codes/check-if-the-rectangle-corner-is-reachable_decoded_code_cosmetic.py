class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        VISIT = [False] * len(circles)

        def isInside(u, v, a, b, radius):
            return (u - a) ** 2 + (v - b) ** 2 <= radius ** 2

        def touchesLeftTopEdge(centerX, centerY, rad):
            condition_one = (abs(centerX) <= rad) and (0 <= centerY <= yCorner)
            condition_two = (abs(centerY - yCorner) <= rad) and (0 <= centerX <= xCorner)
            return condition_one or condition_two

        def touchesRightBottomEdge(centerX, centerY, rad):
            condition_one = (abs(centerX - xCorner) <= rad) and (0 <= centerY <= yCorner)
            condition_two = (abs(centerY) <= rad) and (0 <= centerX <= xCorner)
            return condition_one or condition_two

        def depthSearch(idx):
            cx, cy, r = circles[idx]

            if touchesRightBottomEdge(cx, cy, r):
                return True

            VISIT[idx] = True

            def recursiveLoop(j):
                if j == len(circles):
                    return False

                px, py, pr = circles[j]

                if VISIT[j] or (cx - px) ** 2 + (cy - py) ** 2 > (r + pr) ** 2:
                    return recursiveLoop(j + 1)

                # The original pseudocode uses the condition:
                # (cx * pr + px * r) < (r + pr) * xCorner AND (cy * pr + py * r) < (r + pr) * yCorner
                # This condition is a bit unusual; keeping it as provided.
                if (cx * pr + px * r) < (r + pr) * xCorner and (cy * pr + py * r) < (r + pr) * yCorner and depthSearch(j):
                    return True

                return recursiveLoop(j + 1)

            return recursiveLoop(0)

        def repeatCheck(k):
            if k == len(circles):
                return True

            cx, cy, r = circles[k]

            if isInside(0, 0, cx, cy, r) or isInside(xCorner, yCorner, cx, cy, r):
                return False

            if not VISIT[k] and touchesLeftTopEdge(cx, cy, r) and depthSearch(k):
                return False

            return repeatCheck(k + 1)

        return repeatCheck(0)