class Solution:
    def numberOfPairs(self, points):
        resultCounter = 0
        totalPoints = len(points)
        outerIndex = 0

        while outerIndex < totalPoints:
            innerIndex = 0
            while innerIndex < totalPoints:
                if outerIndex != innerIndex:
                    xAlpha, yAlpha = points[outerIndex]
                    xBeta, yBeta = points[innerIndex]
                    if (xAlpha <= xBeta) and (yAlpha >= yBeta):
                        isPairValid = True
                        checkIndex = 0
                        while checkIndex < totalPoints and isPairValid:
                            if checkIndex != outerIndex and checkIndex != innerIndex:
                                xGamma, yGamma = points[checkIndex]
                                if (xAlpha <= xGamma <= xBeta) and (yAlpha >= yGamma >= yBeta):
                                    isPairValid = False
                            if not isPairValid:
                                break
                            checkIndex += 1
                        if isPairValid:
                            resultCounter += 1
                innerIndex += 1
            outerIndex += 1
        return resultCounter