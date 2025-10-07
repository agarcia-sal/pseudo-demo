class Solution:
    def numberOfPairs(self, points):
        def isWithinBounds(a_x, a_y, b_x, b_y, c_x, c_y):
            # Check if (c_x, c_y) is within the rectangle defined by (a_x,a_y) and (b_x,b_y)
            # Given the inequalities from pseudocode:
            # a_x <= c_x <= b_x and a_y >= c_y >= b_y
            return a_x <= c_x <= b_x and a_y >= c_y >= b_y

        def getCoord(coordList, idx, pos):
            return coordList[idx][pos]

        lengthPoints = len(points)
        accCount = 0

        def incrementCounter():
            nonlocal accCount
            accCount += 1

        def areIndicesDifferent(x, y):
            return x != y

        def scanInner(kIn, iIn, jIn, pointsList):
            if areIndicesDifferent(kIn, iIn) and areIndicesDifferent(kIn, jIn):
                x_k = getCoord(pointsList, kIn, 0)
                y_k = getCoord(pointsList, kIn, 1)
                x_i = getCoord(pointsList, iIn, 0)
                y_i = getCoord(pointsList, iIn, 1)
                x_j = getCoord(pointsList, jIn, 0)
                y_j = getCoord(pointsList, jIn, 1)
                if isWithinBounds(x_i, y_i, x_j, y_j, x_k, y_k):
                    return False
            return True

        def innerLoop(iIdx, jIdx, pointsList):
            def recur(kIdx, limit):
                if kIdx == limit:
                    return True
                if not scanInner(kIdx, iIdx, jIdx, pointsList):
                    return False
                return recur(kIdx + 1, limit)
            return recur(0, lengthPoints)

        def conditionCheck(iIdx, jIdx, pointsList):
            x_i = getCoord(pointsList, iIdx, 0)
            y_i = getCoord(pointsList, iIdx, 1)
            x_j = getCoord(pointsList, jIdx, 0)
            y_j = getCoord(pointsList, jIdx, 1)
            return x_i <= x_j and y_i >= y_j

        def outerLoop(iPos):
            if iPos == lengthPoints:
                return
            def nestedLoopFunc(jPosInner):
                if jPosInner == lengthPoints:
                    return
                if areIndicesDifferent(iPos, jPosInner):
                    if conditionCheck(iPos, jPosInner, points):
                        if innerLoop(iPos, jPosInner, points):
                            incrementCounter()
                nestedLoopFunc(jPosInner + 1)
            nestedLoopFunc(0)
            outerLoop(iPos + 1)

        outerLoop(0)
        return accCount