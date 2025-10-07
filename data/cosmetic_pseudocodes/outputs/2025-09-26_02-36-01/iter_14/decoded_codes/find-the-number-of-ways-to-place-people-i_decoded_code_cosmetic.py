class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        limit = len(points)
        for outerIndex in range(limit):
            for innerIndex in range(limit):
                if outerIndex != innerIndex:
                    px, py = points[outerIndex]
                    qx, qy = points[innerIndex]
                    if px <= qx and py >= qy:
                        isValidPair = True
                        for checkIndex in range(limit):
                            if checkIndex != outerIndex and checkIndex != innerIndex:
                                rx, ry = points[checkIndex]
                                if (not (rx < px) and not (qx < rx)) and (not (ry > py) and not (qy > ry)):
                                    isValidPair = False
                                    break
                        if isValidPair:
                            totalPairs += 1
        return totalPairs