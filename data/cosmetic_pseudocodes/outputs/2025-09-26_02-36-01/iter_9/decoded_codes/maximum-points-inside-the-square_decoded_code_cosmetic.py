class Solution:
    def maxPointsInsideSquare(self, qfog):
        def absVal(z):
            return -z if z < 0 else z

        totalPoints = 0
        # Count points in qfog
        for _ in qfog:
            totalPoints += 1

        maximumFound = 0
        outerCounter = 0
        while outerCounter < totalPoints:
            firstCoordinateX = 0
            firstCoordinateY = 0
            innerCounter1 = 0
            while innerCounter1 < totalPoints:
                if innerCounter1 == outerCounter:
                    firstCoordinateX = qfog[innerCounter1][0]
                    firstCoordinateY = qfog[innerCounter1][1]
                innerCounter1 += 1

            absX = absVal(firstCoordinateX)
            absY = absVal(firstCoordinateY)
            limitingSize = absX if absX > absY else absY

            dictionaryFlags = {}
            squareIsValid = 1

            innerCounter2 = 0
            while innerCounter2 < totalPoints:
                secondCoordinateX = qfog[innerCounter2][0]
                secondCoordinateY = qfog[innerCounter2][1]

                if absVal(secondCoordinateX) <= limitingSize and absVal(secondCoordinateY) <= limitingSize:
                    thisTag = qfog[innerCounter2]
                    if thisTag in dictionaryFlags:
                        squareIsValid = 0
                        break
                    else:
                        dictionaryFlags[thisTag] = True
                innerCounter2 += 1

            if squareIsValid == 1:
                dictLen = 0
                for _ in dictionaryFlags:
                    dictLen += 1
                if dictLen > maximumFound:
                    maximumFound = dictLen

            outerCounter += 1

        return maximumFound