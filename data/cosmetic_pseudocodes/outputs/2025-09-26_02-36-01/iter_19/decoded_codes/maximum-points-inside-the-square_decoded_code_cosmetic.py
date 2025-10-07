class Solution:
    def maxPointsInsideSquare(self, s):
        total = len(s)
        peak = 0
        outerIndex = 0
        while outerIndex < total:
            coordX, coordY = s[outerIndex]
            limit = abs(coordX) if abs(coordX) > abs(coordY) else abs(coordY)
            encounteredTags = {}
            isValid = True
            innerIndex = 0
            while True:
                if innerIndex >= total:
                    break
                posX, posY = s[innerIndex]
                if not (abs(posX) > limit) and not (abs(posY) > limit):
                    currentTag = s[innerIndex]
                    if currentTag in encounteredTags:
                        isValid = False
                        break
                    else:
                        encounteredTags[currentTag] = True
                innerIndex += 1
            if isValid:
                peak = max(peak, len(encounteredTags))
            outerIndex += 1
        return peak