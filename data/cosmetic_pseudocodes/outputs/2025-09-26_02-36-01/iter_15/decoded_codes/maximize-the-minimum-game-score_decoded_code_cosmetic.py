class Solution:
    def maxScore(self, points, m):
        from math import floor

        def isPossible(minVal, m):
            totalActions = 0
            previousActions = 0
            indexCounter = 0

            n = len(points)
            while indexCounter < n:
                elementValue = points[indexCounter]
                quotient = (minVal + elementValue - 1) / elementValue
                requiredMoves = floor(quotient)

                if requiredMoves - previousActions < 0:
                    requiredMoves = 0
                else:
                    requiredMoves = requiredMoves - previousActions

                if requiredMoves > 0:
                    totalActions += requiredMoves * 2 - 1
                    previousActions = requiredMoves - 1
                elif (indexCounter + 1) < n:
                    totalActions += 1
                    previousActions = 0

                if totalActions > m:
                    return False

                indexCounter += 1

            return True

        leftBound = 0
        rightBound = ((m + 1) // 2) * (points[0] + 1)

        while leftBound < rightBound:
            middleVal = (leftBound + rightBound + 1) // 2
            if isPossible(middleVal, m):
                leftBound = middleVal
            else:
                rightBound = middleVal - 1

        return leftBound