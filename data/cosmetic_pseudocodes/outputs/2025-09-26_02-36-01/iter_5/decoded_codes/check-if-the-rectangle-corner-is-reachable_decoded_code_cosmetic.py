class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def in_circle(xParam, yParam, cxParam, cyParam, radiusParam):
            deltaX = xParam - cxParam
            deltaY = yParam - cyParam
            distSquared = (deltaX * deltaX) + (deltaY * deltaY)
            radiusSquared = radiusParam * radiusParam
            return distSquared <= radiusSquared

        def cross_left_top(cxParam, cyParam, radiusParam):
            condA = (abs(cxParam) <= radiusParam) and (0 <= cyParam <= yCorner)
            diffYCorner = abs(cyParam - yCorner)
            condB = (diffYCorner <= radiusParam) and (0 <= cxParam <= xCorner)
            return condA or condB

        def cross_right_bottom(cxParam, cyParam, radiusParam):
            diffXCorner = abs(cxParam - xCorner)
            condA = (diffXCorner <= radiusParam) and (0 <= cyParam <= yCorner)
            condB = (abs(cyParam) <= radiusParam) and (0 <= cxParam <= xCorner)
            return condA or condB

        vis = []
        def init_vis(counter):
            if counter == len(circles):
                return
            vis.append(False)
            init_vis(counter + 1)
        init_vis(0)

        def dfs(indexCircle):
            circleInfo = circles[indexCircle]
            posX, posY, rad = circleInfo[0], circleInfo[1], circleInfo[2]

            if cross_right_bottom(posX, posY, rad):
                return True

            vis[indexCircle] = True

            def recur(currentJ):
                if currentJ == len(circles):
                    return False

                otherCircle = circles[currentJ]
                oX, oY, oR = otherCircle[0], otherCircle[1], otherCircle[2]

                if vis[currentJ]:
                    return recur(currentJ + 1)

                distX = posX - oX
                distY = posY - oY
                distSumSquared = (distX * distX) + (distY * distY)
                radiusSum = rad + oR
                radiusSumSquared = radiusSum * radiusSum

                if distSumSquared > radiusSumSquared:
                    return recur(currentJ + 1)

                lhsX = (posX * oR) + (oX * rad)
                rhsX = radiusSum * xCorner
                lhsY = (posY * oR) + (oY * rad)
                rhsY = radiusSum * yCorner

                if (lhsX < rhsX) and (lhsY < rhsY):
                    if dfs(currentJ):
                        return True
                    else:
                        return recur(currentJ + 1)
                else:
                    return recur(currentJ + 1)

            return recur(0)

        def loop_circles(iInstance):
            if iInstance == len(circles):
                return True

            circleElement = circles[iInstance]
            cX, cY, cR = circleElement[0], circleElement[1], circleElement[2]

            if in_circle(0, 0, cX, cY, cR) or in_circle(xCorner, yCorner, cX, cY, cR):
                return False

            if (not vis[iInstance]) and cross_left_top(cX, cY, cR) and dfs(iInstance):
                return False

            return loop_circles(iInstance + 1)

        result = loop_circles(0)
        return result