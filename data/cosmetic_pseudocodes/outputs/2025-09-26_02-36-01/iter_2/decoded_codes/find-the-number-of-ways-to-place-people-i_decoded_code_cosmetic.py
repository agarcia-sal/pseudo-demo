class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        lengthPoints = len(points)
        outerIndex = 0
        while outerIndex < lengthPoints:
            innerIndex = 0
            while innerIndex < lengthPoints:
                if outerIndex != innerIndex:
                    xStart, yStart = points[outerIndex]
                    xEnd, yEnd = points[innerIndex]
                    if xStart <= xEnd and yStart >= yEnd:
                        isValidPair = True
                        checkIndex = 0
                        while checkIndex < lengthPoints:
                            if checkIndex != outerIndex and checkIndex != innerIndex:
                                xMid, yMid = points[checkIndex]
                                if xStart <= xMid <= xEnd and yStart >= yMid >= yEnd:
                                    isValidPair = False
                                    break
                            checkIndex += 1
                        if isValidPair:
                            totalPairs += 1
                innerIndex += 1
            outerIndex += 1
        return totalPairs