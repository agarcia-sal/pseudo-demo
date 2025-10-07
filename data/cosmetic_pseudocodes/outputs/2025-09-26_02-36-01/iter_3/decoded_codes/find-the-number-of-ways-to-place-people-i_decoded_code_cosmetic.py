class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        lengthPoints = len(points)
        for outerIndex in range(lengthPoints):
            for innerIndex in range(lengthPoints):
                if outerIndex != innerIndex:
                    xiVal, yiVal = points[outerIndex]
                    xjVal, yjVal = points[innerIndex]
                    if (xiVal <= xjVal) and (yiVal >= yjVal):
                        isValid = True
                        for checkIndex in range(lengthPoints):
                            if checkIndex != outerIndex and checkIndex != innerIndex:
                                xkVal, ykVal = points[checkIndex]
                                if (xiVal <= xkVal <= xjVal) and (yiVal >= ykVal >= yjVal):
                                    isValid = False
                                    break
                        if isValid:
                            totalPairs += 1
        return totalPairs