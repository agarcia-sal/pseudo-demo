class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        length = len(points)

        def checkValidity(startIdx, endIdx):
            sx, sy = points[startIdx]
            ex, ey = points[endIdx]

            for idx in range(length):
                if idx != startIdx and idx != endIdx:
                    px, py = points[idx]
                    if (sx <= px <= ex) and (sy >= py >= ey):
                        return False
            return True

        for outerIdx in range(length):
            for innerIdx in range(length):
                if outerIdx != innerIdx:
                    outerX, outerY = points[outerIdx]
                    innerX, innerY = points[innerIdx]
                    if outerX <= innerX and outerY >= innerY:
                        if checkValidity(outerIdx, innerIdx):
                            totalPairs += 1

        return totalPairs