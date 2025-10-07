class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        limit = len(points)
        outerIdx = 0
        while outerIdx < limit:
            innerIdx = 0
            while innerIdx < limit:
                if outerIdx != innerIdx:
                    px, py = points[outerIdx]
                    qx, qy = points[innerIdx]
                    if px <= qx and py >= qy:
                        isValid = 1
                        checker = 0
                        while checker < limit:
                            if checker != outerIdx and checker != innerIdx:
                                rx, ry = points[checker]
                                if px <= rx <= qx and py >= ry >= qy:
                                    isValid = 0
                                    break
                            checker += 1
                        if isValid == 1:
                            totalPairs += 1
                innerIdx += 1
            outerIdx += 1
        return totalPairs