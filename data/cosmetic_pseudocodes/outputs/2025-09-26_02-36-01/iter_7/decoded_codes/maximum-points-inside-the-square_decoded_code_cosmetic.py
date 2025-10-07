class Solution:
    def maxPointsInsideSquare(self, s):
        lengthPoints = len(s)
        maximumPoints = 0

        outerIndex = 0
        while outerIndex <= lengthPoints - 1:
            coordX = s[outerIndex][0]
            coordY = s[outerIndex][1]

            if abs(coordX) > abs(coordY):
                boundary = abs(coordX)
            else:
                boundary = abs(coordY)

            identifierMap = {}
            isSquareValid = True

            innerCounter = 0
            while True:
                if innerCounter > lengthPoints - 1:
                    break

                currentX = s[innerCounter][0]
                currentY = s[innerCounter][1]

                if not (abs(currentX) > boundary or abs(currentY) > boundary):
                    tagLabel = s[innerCounter]
                    if tagLabel in identifierMap:
                        isSquareValid = False
                        innerCounter = lengthPoints  # early break from inner loop
                    else:
                        identifierMap[tagLabel] = True

                innerCounter += 1

            if isSquareValid:
                if len(identifierMap) > maximumPoints:
                    maximumPoints = len(identifierMap)

            outerIndex += 1

        return maximumPoints