class Solution:
    def maxPointsInsideSquare(self, s):
        totalCount = len(s)
        maximumResult = 0
        outerIndex = 0
        while outerIndex < totalCount:
            coordX, coordY = s[outerIndex]
            limitSide = abs(coordX) if abs(coordX) >= abs(coordY) else abs(coordY)
            encounteredTags = {}
            isSquareValid = True
            innerIndex = 0
            while innerIndex < totalCount and isSquareValid:
                currentX, currentY = s[innerIndex]
                if abs(currentX) <= limitSide and abs(currentY) <= limitSide:
                    currentTag = s[innerIndex]
                    if currentTag in encounteredTags:
                        isSquareValid = False
                    else:
                        encounteredTags[currentTag] = True
                innerIndex += 1
            if isSquareValid:
                if len(encounteredTags) > maximumResult:
                    maximumResult = len(encounteredTags)
            outerIndex += 1
        return maximumResult