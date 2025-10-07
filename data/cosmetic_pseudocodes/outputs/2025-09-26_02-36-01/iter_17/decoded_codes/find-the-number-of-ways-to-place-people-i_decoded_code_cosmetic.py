class Solution:
    def numberOfPairs(self, points):
        total = 0
        length = len(points)
        outerIndex = 0
        while outerIndex < length:
            innerIndex = 0
            while innerIndex < length:
                if outerIndex != innerIndex:
                    px, py = points[outerIndex]
                    qx, qy = points[innerIndex]
                    if not (qx < px) and not (py < qy):
                        isValid = True
                        middleIndex = 0
                        while middleIndex < length and isValid:
                            if middleIndex != outerIndex and middleIndex != innerIndex:
                                rx, ry = points[middleIndex]
                                if (px <= rx <= qx) and (py >= ry >= qy):
                                    isValid = False
                            middleIndex += 1
                        if isValid:
                            total += 1
                innerIndex += 1
            outerIndex += 1
        return total